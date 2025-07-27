from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.views.decorators.csrf import csrf_protect
from .forms import ExampleForm

#my inclusions
from django.http import HttpResponse

# Create your views here.
@csrf_protect
def index(request):
    response = "Welcome to the Book shelf 📚"
    return HttpResponse(response)

@csrf_protect
@permission_required('bookshelf.can_edit', raise_exception=True)
def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'relationship_app/list_books.html', context)

# ============= Test SECURE_PROXY_SSL_HEADER = 'HTTP_X_FORWARDED_PROTO' =============
from django.http import HttpResponse
import logging

logger = logging.getLogger('django.request')

def check_secure(request):
    logger.info(f"[SECURE CHECK] is_secure: {request.is_secure()} | Scheme: {request.scheme} | Header: {request.META.get('HTTP_X_FORWARDED_PROTO')}")
    return HttpResponse("Check complete. See server logs.")