from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.book = Book.objects.create(
            title="Test Book",
            author="Author Name",
            published_date="2024-01-01"
        )
        self.list_url = reverse("book-list")

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "published_date": "2024-02-01"
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # 🔑 CHECK RESPONSE DATA
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["author"], data["author"])

    def test_get_books(self):
        response = self.client.get(self.list_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 🔑 ENSURE DATA IS RETURNED
        self.assertIn("title", response.data[0])
        self.assertIn("author", response.data[0])

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book.id])
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "published_date": "2024-03-01"
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 🔑 VERIFY UPDATED DATA
        self.assertEqual(response.data["title"], "Updated Book")
        self.assertEqual(response.data["author"], "Updated Author")

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
