from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list_books/<int:book_id>/", views.list_books, name="list_book"),
    path("check_secure/", views.check_secure, name="check_secure"),
]