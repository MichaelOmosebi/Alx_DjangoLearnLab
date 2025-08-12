from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Author, Book

from rest_framework import status
from django.test import TestCase
from .views import DetailView

User = get_user_model()

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Login the user
        self.client.login(username="testuser", password="testpass123")

        # Create an author
        self.author_data = {"name": "Me Myself TestCase"}
        self.author_response = self.client.post(reverse("author-list"), self.author_data, format="json")
        self.author_id = self.author_response.data["id"]

        # Create a sample book
        self.book_data = {
            "title": "Me Myself TestCase",
            "description": "A sample book for testing.",
            "author": self.author_id
        }
        self.client.post(reverse("book-list"), self.book_data, format="json")


    def test_list_books(self):
        """Test that books can be listed without authentication."""
        self.client.logout()
        response = self.client.get(reverse("book-list"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book(self):
        """Test that an authenticated user can create a book."""
        data = {
            "title": "New Book",
            "description": "Another book for testing.",
            "author": self.author_id
        }
        response = self.client.post(reverse("book-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_update_book(self):
        """Test that an authenticated user can update a book."""
        book_id = 1
        updated_data = {
            "title": "Updated Book",
            "description": "Updated description",
            "author": self.author_id
        }
        response = self.client.put(reverse("book-detail", args=[book_id]), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_delete_book(self):
        """Test that an authenticated user can delete a book."""
        book_id = 1
        response = self.client.delete(reverse("book-detail", args=[book_id]), format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(response.data), 1)
