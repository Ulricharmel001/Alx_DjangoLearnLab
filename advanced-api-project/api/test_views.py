from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book




class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

        # Create a sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="Author One",
            published_date="2024-01-01",
            isbn="1234567890123",
            pages=100,
            language="EN",
            publisher="Test Publisher"
        )

        # URLs
        self.book_list_url = reverse('book-list')  # assumes DRF router
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.id})

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "Author Two",
            "published_date": "2024-02-01",
            "isbn": "9876543210987",
            "pages": 200,
            "language": "FR",
            "publisher": "New Publisher"
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.book.title)

    def test_update_book(self):
        data = {"title": "Updated Title"}
        response = self.client.patch(self.book_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permission_required(self):
        # Logout user
        self.client.logout()
        response = self.client.post(self.book_list_url, {"title": "Unauthorized"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
