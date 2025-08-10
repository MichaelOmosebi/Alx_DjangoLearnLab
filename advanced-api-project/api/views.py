from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django_filters import rest_framework

# import django_filters.rest_framework

# Create your views here.
# updated

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]

    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend] #optional to declaring globally within the App in the settings.py file
    filter_fields = ['title', 'author', 'publication_year']

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


# Customization Instructions:
# Customize the CreateView and UpdateView to ensure they properly handle form submissions and data validation.
# Integrate additional functionalities such as permission checks or filters directly into the views using DRF’s built-in features or custom methods.
# Step 3: Customize View Behavior
# Customization Instructions:
# Customize the CreateView and UpdateView to ensure they properly handle form submissions and data validation.
# Integrate additional functionalities such as permission checks or filters directly into the views using DRF’s built-in features or custom methods.
# Step 4: Implement Permissions
# Permissions Setup:
# Apply Django REST Framework’s permission classes to protect API endpoints based on user roles.
# For example, restrict CreateView, UpdateView, and DeleteView to authenticated users only, while allowing read-only access to unauthenticated users for ListView and DetailView.
