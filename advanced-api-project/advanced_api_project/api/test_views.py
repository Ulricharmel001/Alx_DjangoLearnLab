from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='Jane Doe')
        self.book = Book.objects.create(title='Django Advanced', publication_year=2023, author=self.author)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {'title': 'REST API', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        data = {'title': 'Updated Title', 'publication_year': 2023, 'author': self.author.id}
        response = self.client.put(f'/api/books/{self.book.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
