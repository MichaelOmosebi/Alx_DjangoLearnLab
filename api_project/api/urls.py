from django.urls import path
from .views import BookList
# URL patterns for the API
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
# This will handle both listing all books and creating a new book