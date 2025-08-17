### Book API Endpoints

- GET /books/ → List all books (public)
- GET /books/<id>/ → Retrieve a book (public)
- POST /books/create/ → Create a new book (authenticated only)
- PUT /books/<id>/update/ → Update a book (authenticated only)
- DELETE /books/<id>/delete/ → Delete a book (authenticated only)

Permissions:
- Unauthenticated users: Read-only
- Authenticated users: Full 



# API Testing

I used Django’s test framework with DRF’s APITestCase.

## Run Tests
```bash
python manage.py test api

