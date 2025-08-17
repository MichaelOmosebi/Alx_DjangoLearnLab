from django.urls import path
from django.contrib.auth import views as auth_views
from .views import BlogsView

app_name = 'blog'   # 👈 this gives it the 'blog:' namespace

urlpatterns = [
    path('blogs/', BlogsView.as_view(), name='home'),
]

app_name = 'blog'   # 👈 this gives it the 'blog:' namespace

# urlpatterns = [
#     path('', views.home, name='home'),  # home view
# ]