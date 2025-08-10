from django.urls import path
from .views import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)


urlpatterns = [
    path('books/create/', CreateView.as_view(), name='create-book'),
    path('books/<int:pk>/', DetailView.as_view(), name='retrieve-book'),
    path('books/', ListView.as_view(), name='list-books'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='update-book'),
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='delete-book'),
]