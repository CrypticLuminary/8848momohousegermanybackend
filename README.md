# 8848 Momo House Germany Backend

Django 5 + DRF CMS-first backend for the existing React/Vercel frontend.

## Local Setup

Fast path for local testing:

```powershell
python scripts.py
```

This creates `.venv`, installs requirements, migrates, seeds CMS content, creates/resets `admin / pass`, and starts the backend at `http://127.0.0.1:4000`.

Manual setup:

```powershell
cd C:\Project\GUSTO\8848momohousegermanybackend
py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements/development.txt
copy .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_initial_content
python manage.py runserver 4000
```

Python is not installed in the Codex sandbox, so migrations should be generated on your machine with `python manage.py makemigrations`.

## Production

Use `config.settings.production` with Railway or Render.

```text
DJANGO_SETTINGS_MODULE=config.settings.production
SECRET_KEY=...
DEBUG=False
DATABASE_URL=...
ALLOWED_HOSTS=your-backend-domain
CORS_ALLOWED_ORIGINS=https://8848momohouse.vercel.app
MEDIA_ROOT=/app/media
```

Start command:

```bash
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi:application
```

The included `Procfile` runs those same production steps for hosts that support it.

## Main Endpoints

- `GET /api/v1/health/`
- `POST /api/v1/auth/token/`
- `POST /api/v1/auth/token/refresh/`
- `GET /api/v1/cms/pages/`
- `GET /api/v1/cms/pages/<slug>/`
- `GET /api/v1/menu/current/`
- `GET /api/v1/menu/documents/`
- `GET /api/v1/menu/pages/?document=<slug>`
- `GET /api/v1/navigation/`
- `GET /api/v1/gallery/`
- `GET /api/v1/locations/`
- `GET /api/v1/testimonials/`
- `GET /api/v1/franchise/faq/`
- `POST /api/v1/franchise/inquiries/`
- `GET /api/v1/settings/`

Admin CRUD APIs live under `/api/v1/admin/*` and require JWT admin access. Restaurant staff should normally use `/admin/`.

## Important Frontend Match

The current React menu UI is image-based, not item/category based. The backend menu app therefore manages:

- `MenuDocument`: page title, kicker, subtitle, footer copy, default active menu
- `MenuPageImage`: uploaded or existing public menu page images, ordering, alt text, lightbox captions

This maps directly to the existing `MomoFlipBook` and menu lightbox UI.
