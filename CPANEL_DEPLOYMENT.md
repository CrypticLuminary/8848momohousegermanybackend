# cPanel Passenger Deployment Runbook

Sensitive values must not be written into this file. Use cPanel Environment Variables or a protected `.env`.

## Discovered Paths

- Local backend project: `C:\Project\GUSTO\8848momohousegermanybackend`
- cPanel user from screenshot: `kjqwnupszi`
- cPanel home from screenshot: `/home/kjqwnupszi`
- Recommended cPanel application root: `/home/kjqwnupszi/8848momohousegermanybackend`
- Startup file: `passenger_wsgi.py`
- Application entry point: `application`
- Django settings module: `config.settings.production`
- Static root after `collectstatic`: `/home/kjqwnupszi/8848momohousegermanybackend/staticfiles`
- Media root: `/home/kjqwnupszi/8848momohousegermanybackend/media`
- Temporary SQLite database path, if used: `/home/kjqwnupszi/8848momohousegermanybackend/db.sqlite3`
- Typical cPanel virtualenv path: `/home/kjqwnupszi/virtualenv/8848momohousegermanybackend/3.12/bin/activate`

## Setup Python App

Use cPanel `Setup Python App`.

- Python version: choose Python `3.12` if available. The repo asks for `python-3.12.4`; cPanel may show a nearby patch version.
- Application root: `8848momohousegermanybackend`
- Application URL: use the final backend domain/subdomain, for example `api.your-domain.example`.
- Application startup file: `passenger_wsgi.py`
- Application entry point: `application`

After cPanel creates the app, note the exact virtualenv activation command shown by cPanel. It usually resembles:

```bash
source /home/kjqwnupszi/virtualenv/8848momohousegermanybackend/3.12/bin/activate && cd /home/kjqwnupszi/8848momohousegermanybackend
```

## Environment Variables

Set these in cPanel `Setup Python App` Environment Variables, or in a protected `.env` inside the app root.

```text
DJANGO_SETTINGS_MODULE=config.settings.production
DEBUG=False
SECRET_KEY=<generate-strong-secret-do-not-log>
ALLOWED_HOSTS=<backend-domain>,www.<backend-domain>
CSRF_TRUSTED_ORIGINS=https://<backend-domain>,https://www.<backend-domain>
CORS_ALLOWED_ORIGINS=https://<frontend-domain>
MEDIA_ROOT=/home/kjqwnupszi/8848momohousegermanybackend/media
```

Database option A, temporary SQLite:

```text
DATABASE_URL=sqlite:////home/kjqwnupszi/8848momohousegermanybackend/db.sqlite3
```

Database option B, cPanel PostgreSQL if available:

```text
DATABASE_URL=postgres://<user>:<password>@<host>:<port>/<database>
```

Database option C, cPanel MySQL/MariaDB:

```text
DATABASE_URL=mysql://<user>:<password>@<host>:3306/<database>
```

If using MySQL/MariaDB, install and verify a Django MySQL driver first, typically `mysqlclient`. Do not switch to MySQL until credentials and driver installation are confirmed.

## Install Commands

Run these in cPanel Terminal after activating the cPanel-created virtualenv.

```bash
cd /home/kjqwnupszi/8848momohousegermanybackend
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements/production.txt
python manage.py migrate --settings=config.settings.production
python manage.py seed_initial_content --settings=config.settings.production
python manage.py collectstatic --noinput --settings=config.settings.production
python manage.py check --deploy --settings=config.settings.production
```

If using SQLite temporarily, verify file permissions:

```bash
ls -la /home/kjqwnupszi/8848momohousegermanybackend/db.sqlite3
ls -ld /home/kjqwnupszi/8848momohousegermanybackend
ls -ld /home/kjqwnupszi/8848momohousegermanybackend/media
```

## Restart

Use cPanel `Setup Python App` > `Restart`, or run:

```bash
mkdir -p /home/kjqwnupszi/8848momohousegermanybackend/tmp
touch /home/kjqwnupszi/8848momohousegermanybackend/tmp/restart.txt
```

## Public Tests

Replace `<backend-url>` with the final HTTPS backend URL.

```bash
curl -I https://<backend-url>/
curl https://<backend-url>/api/v1/health/
curl -I https://<backend-url>/admin/
curl https://<backend-url>/api/v1/settings/
curl https://<backend-url>/api/v1/navigation/
curl https://<backend-url>/api/v1/menu/current/
```

Admin login and Studio login must be tested manually after a production admin user is created.

## Frontend Production Requirement

The frontend must be rebuilt/redeployed with the backend URL:

```text
VITE_CMS_API_URL=https://<backend-url>
VITE_API_URL=https://<backend-url>
```

Also include the frontend domain in backend `CORS_ALLOWED_ORIGINS`.

## HTTPS

In cPanel:

1. Confirm the backend domain/subdomain points to this hosting account.
2. Open `SSL/TLS Status`.
3. Run AutoSSL for the backend domain if no certificate exists.
4. Confirm public URL uses `https://`.

Keep `SESSION_COOKIE_SECURE=True` and `CSRF_COOKIE_SECURE=True` in production.

## Rollback

- Restore settings backup if needed: `config/settings/production.py.bak-20260528-cpanel`
- Remove or rename `passenger_wsgi.py` only if cPanel startup must be regenerated.
- Restore database from cPanel backup before destructive migration rollback.
- If app fails after deploy, check cPanel Passenger error log first, then temporarily run `python manage.py check --settings=config.settings.production` inside the cPanel virtualenv.

