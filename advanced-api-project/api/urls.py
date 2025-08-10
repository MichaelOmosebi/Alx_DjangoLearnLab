from django.urls import path
from .views import (
    CreateBookView,
    RetrieveBookView,
    ListBooksView,
    UpdateBookView,
    DeleteBookView
)


url_patterns = [
    path('books/create/', CreateBookView.as_view(), name='create-book'),
    path('books/<int:pk>/', RetrieveBookView.as_view(), name='retrieve-book'),
    path('books/', ListBooksView.as_view(), name='list-books'),
    path('books/<int:pk>/update/', UpdateBookView.as_view(), name='update-book'),
    path('books/<int:pk>/delete/', DeleteBookView.as_view(), name='delete-book'),
]