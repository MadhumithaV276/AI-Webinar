# ManufactureAI Webinar Registration (Django)

This project uses your supplied AI for Manufacturing landing page and adds a Django backend, database storage, an admin dashboard, search, edit/delete, and CSV export.

## 1. Requirements
- Python 3.10+
- Optional: MySQL Server + MySQL Workbench (SQLite works immediately for local testing)

## 2. Setup on Windows (PowerShell)
Open PowerShell in this project folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If PowerShell blocks activation, use:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Open:
- Webinar page: http://127.0.0.1:8000/
- Admin dashboard login: http://127.0.0.1:8000/admin-login/
- Django admin (optional): http://127.0.0.1:8000/django-admin/

Use the username/password created by `createsuperuser`. The dashboard is restricted to staff/superuser accounts.

## 3. Use MySQL instead of SQLite (optional)
Create a database in MySQL Workbench:
```sql
CREATE DATABASE manufactureai CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
Set these environment variables in PowerShell before starting Django:
```powershell
$env:DB_ENGINE="mysql"
$env:DB_NAME="manufactureai"
$env:DB_USER="root"
$env:DB_PASSWORD="YOUR_MYSQL_PASSWORD"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
```
Then run:
```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Keep your database password private. Do not commit it to GitHub.

## 4. How it works
1. A visitor submits the webinar form.
2. Django validates the data and saves it in the `Registration` table.
3. The visitor sees a confirmation page.
4. A staff admin logs in to `/admin-login/` and manages registrations at `/dashboard/`.
5. Use Export CSV to download participant details for Excel.

The app prevents duplicate email registrations for this webinar. Payment is not collected or verified by this project; ticket choice is recorded only.

## 5. Important before deployment
- Set `DJANGO_DEBUG=False`.
- Set a strong, private `DJANGO_SECRET_KEY`.
- Set `DJANGO_ALLOWED_HOSTS` to your real domain.
- Use HTTPS and a production database.
- Configure secure cookies and backups for production.
- Do not expose the admin dashboard publicly without strong admin passwords.
