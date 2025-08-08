# Security Measures Implemented

- DEBUG set to False in production.
- ALLOWED_HOSTS configured.
- CSRF protection enabled with {% csrf_token %} in all forms.
- Views protected by Django's @permission_required decorators for create, edit, delete operations.
- User inputs are validated using Django ModelForms.
- Content Security Policy (CSP) set via django-csp middleware to reduce XSS risks.
- Cookies set as secure and HttpOnly flags where applicable.
- Static files served securely using WhiteNoise in production.
