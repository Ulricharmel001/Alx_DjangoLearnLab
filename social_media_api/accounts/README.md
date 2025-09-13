# social_media_api (Alx_DjangoLearnLab)

## Setup
1. python -m venv .venv && source .venv/bin/activate
3. set AUTH_USER_MODEL = 'accounts.User' in settings.py
4. python manage.py makemigrations && python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

## Endpoints
- POST /api/accounts/register/  -> register (returns token)
- POST /api/accounts/login/     -> login (returns token)
- GET  /api/accounts/profile/   -> current user profile (auth required)
- GET  /api/accounts/profile/<username>/ -> other user's profile

## Authentication
Use header: `Authorization: Token <token>`

## Set up
social_media_api/
├─ social_media_api/
│  ├─ settings.py
│  ├─ urls.py
│  └─ ...
├─ accounts/
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  ├─ urls.py
│  └─ migrations/
└─ manage.py

