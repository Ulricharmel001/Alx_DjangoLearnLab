# Security Measures Implemented

- DEBUG set to False in production.
- ALLOWED_HOSTS configured.
- CSRF protection enabled with {% csrf_token %} in all forms.
- Views protected by Django's @permission_required decorators for create, edit, delete operations.
- User inputs are validated using Django ModelForms.
- Content Security Policy (CSP) set via django-csp middleware to reduce XSS risks.
- Cookies set as secure and HttpOnly flags where applicable.
- Static files served securely using WhiteNoise in production.



# Security Configuration

## HTTPS
- Enforced using `SECURE_SSL_REDIRECT = True` (production only).
- HSTS enabled: `SECURE_HSTS_SECONDS = 31536000`, with subdomains and preload.

## Cookies
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` ensure cookies are sent over HTTPS only.

## Secure Headers
- `X_FRAME_OPTIONS = 'DENY'` prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True` enables browser XSS protection.

## Deployment
- Use Let's Encrypt for free SSL/TLS.
- Configure Nginx or Apache to serve HTTPS traffic.
