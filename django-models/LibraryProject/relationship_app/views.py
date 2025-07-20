from django.shortcuts import render

# Create your views here.
from relationship_app.models import Book, Library
from django.views.generic import DetailView

def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'books/book_list.html', context)

class BookDetailView(DetailView):
  """A class-based view for displaying details of a specific book."""
  model = Book
  template_name = 'relationship_app/book_detail.html'

  def get_context_data(self, **kwargs):
    """Injects additional context data specific to the book."""
    context = super().get_context_data(**kwargs)  # Get default context data
    book = self.get_object()  # Retrieve the current book instance
    context['average_rating'] = book.get_average_rating()
    return context
  

# Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
# Utilize Django’s ListView or DetailView to structure this class-based view.
class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the library."""
        context = super().get_context_data(**kwargs)  # Get default context data
        library = self.get_object()  # Retrieve the current library instance
        context['books'] = library.books.all()  # List all books in the library
        return context
    

# Note: Ensure that the template files 'books/book_list.html', 'books/book_detail.html', and 'libraries/library_detail.html' exist in your templates directory.
# This code defines views for listing books and displaying details of a specific book and library in a Django application.

# Ensure that the necessary models (Book, Library) are defined in relationship_app/models.py.

