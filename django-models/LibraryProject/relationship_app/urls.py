
from django.urls import path
from . import views
from .views import list_books, BookDetailView, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", list_books, name="book_list"),
    path("books/", BookDetailView.as_view(), name="book_detail"),
    path("libraries/", views.LibraryDetailView.as_view(), name="library_detail"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]

# Configure URL Patterns:
# Edit relationship_app/urls.py to include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.

# This will allow users to access the book list, book details, and library details through the specified URLs.
# Ensure that the URLs are correctly mapped to the views in your Django application.
