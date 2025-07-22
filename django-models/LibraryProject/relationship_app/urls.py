
from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LibraryListView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("book_list/", list_books, name="book_list"),
    path("libraries/", LibraryListView.as_view(), name="library_detail"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', views.register.as_view(), name='register'),
    path("librarian_view/", views.librarian_view, name="librarian_view"),
    path("member_view/", views.member_view, name="member_view"),
    path("admin_view/", views.admin_view, name="admin_view"),
]

# Configure URL Patterns:
# Edit relationship_app/urls.py to include URL patterns that route to the newly created views. Make sure to link both the function-based and class-based views.

# This will allow users to access the book list, book details, and library details through the specified URLs.
# Ensure that the URLs are correctly mapped to the views in your Django application.
