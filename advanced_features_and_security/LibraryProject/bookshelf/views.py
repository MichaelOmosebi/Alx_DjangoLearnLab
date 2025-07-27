from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

#my inclusions
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = "Welcome to the Book shelf 📚"
    return HttpResponse(response)

@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    response = f"Edit book with ID: {book_id}"
    return HttpResponse(response)
