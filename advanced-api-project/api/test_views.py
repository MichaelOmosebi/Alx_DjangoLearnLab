from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework import status
from django.test import TestCase
from .views import DetailView

# Using the standard RequestFactory API to create a form POST request

# request = factory.post('/books/', {
#             'title': 'API TestCase Sample Book',
#             'author': 'API TestCase Sample Author',
#             'publication_year': 2025,
#         })

class BookTests(TestCase):
    def test_book_view(self):
        factory = APIRequestFactory()
        request = factory.get('/books/')

        response = DetailView(request)
        self.assertEqual(request.method, response.status_code)

    def test_create_book(self):
        factory = APIRequestFactory()
        request = factory.post('/books/', {
            'title': 'API TestCase Sample Book',
            'author': 'API TestCase Sample Author',
            'publication_year': 2025,
        }, content_type='json')
        self.assertEqual(request.method, 'POST')

# Test the filtering, searching, and ordering functionalities to verify they work as intended.
# Ensure that permissions and authentication mechanisms are correctly enforcing access controls.

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = DetailView.as_view()

    def test_get_book(self):
        request = self.factory.get('/books/1/')
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_create_book(self):
        request = self.factory.post('/books/', {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2023,
        }, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 201)

    def test_update_book(self):
        request = self.factory.put('/books/1/', {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': 2024,
        }, format='json')
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        request = self.factory.delete('/books/1/')
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(response.data), 1)
