#!/usr/bin/env python
"""One-command local backend setup for reviewers and QA.

Run from the backend folder:

    python scripts.py

The script creates a virtualenv, installs requirements, prepares a local env
file when missing, runs migrations and seed data, creates/resets admin/pass,
then starts the Django development server on 127.0.0.1:4000.
"""

from __future__ import annotations

import os
import subprocess
import sys
import venv
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
IS_WINDOWS = os.name == "nt"
PYTHON = VENV_DIR / ("Scripts/python.exe" if IS_WINDOWS else "bin/python")
PIP = VENV_DIR / ("Scripts/pip.exe" if IS_WINDOWS else "bin/pip")
ENV_FILE = ROOT / ".env"


ENV_TEMPLATE = """SECRET_KEY=local-dev-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
CSRF_TRUSTED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
MEDIA_ROOT=media
"""


def run(command: list[str], message: str) -> None:
    print(f"\n==> {message}")
    subprocess.run(command, cwd=ROOT, check=True)


def ensure_venv() -> None:
    if PYTHON.exists():
        print(f"==> Using existing virtualenv: {VENV_DIR}")
        return
    print(f"==> Creating virtualenv: {VENV_DIR}")
    venv.EnvBuilder(with_pip=True).create(VENV_DIR)


def ensure_env() -> None:
    if ENV_FILE.exists():
        print("==> Using existing .env")
        return
    print("==> Creating local .env")
    ENV_FILE.write_text(ENV_TEMPLATE, encoding="utf-8")


def ensure_admin_user() -> None:
    code = """
from django.contrib.auth import get_user_model
User = get_user_model()
user, _ = User.objects.get_or_create(username="admin", defaults={"email": "admin@example.com"})
user.email = user.email or "admin@example.com"
user.is_staff = True
user.is_superuser = True
if hasattr(user, "role"):
    user.role = "superadmin"
user.set_password("pass")
user.save()
print("Admin user ready: admin / pass")
"""
    run([str(PYTHON), "manage.py", "shell", "-c", code], "Creating or resetting superuser admin / pass")


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
    ensure_venv()
    ensure_env()
    run([str(PYTHON), "-m", "pip", "install", "--upgrade", "pip"], "Upgrading pip")
    run([str(PIP), "install", "-r", "requirements/development.txt"], "Installing backend requirements")
    run([str(PYTHON), "manage.py", "migrate"], "Running database migrations")
    run([str(PYTHON), "manage.py", "seed_initial_content"], "Seeding CMS starter content")
    ensure_admin_user()

    print("\nBackend is ready.")
    print("Admin login: admin / pass")
    print("API: http://127.0.0.1:4000/api/v1/health/")
    print("Django admin: http://127.0.0.1:4000/admin/")
    print("\n==> Starting Django development server")
    subprocess.run([str(PYTHON), "manage.py", "runserver", "127.0.0.1:4000"], cwd=ROOT, check=True)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"\nCommand failed with exit code {exc.returncode}.", file=sys.stderr)
        sys.exit(exc.returncode)
