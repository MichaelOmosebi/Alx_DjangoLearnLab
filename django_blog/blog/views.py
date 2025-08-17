from django.shortcuts import render
from django.views import View
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# # Create your views here.
# Authentication Views:
# Utilize Django’s built-in authentication views and forms to handle user login and logout. For registration and profile management, custom views will be created.
# Extend Django’s UserCreationForm for the registration form to include additional fields like email.

class BlogsView(View):
    def get(self, request):
        # return HttpResponse("This is the blog home page")
        return render(request, 'blog/home.html')
