from .models import Book, Author
from rest_framework import serializers
from django.utils import timezone


#create serializers

# Serializer Details:

# Create a BookSerializer that serializes all fields of the Book model.
# Create an AuthorSerializer that includes:
# The name field.
# A nested BookSerializer to serialize the related books dynamically.
# Validation Requirements:

# Add custom validation to the BookSerializer to ensure the publication_year is not in the future.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_published_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
