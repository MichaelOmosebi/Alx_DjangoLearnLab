# File: Alx_DjangoLearnLab/django-models/LibraryProject/relationship_app/query_samples.py
# --- a/file:///c%3A/Users/Micheal/Videos/ALX BE/django/intro_to_django/Alx_DjangoLearnLab/Alx_DjangoLearnLab/django-models/LibraryProject/relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None
    
#List all books in a library.
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return None
    

# Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None