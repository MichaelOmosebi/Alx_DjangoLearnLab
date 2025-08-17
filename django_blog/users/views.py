from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # log the user in right after registration
#             return redirect('blog:home')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/register.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created for {user.username}! You can now log in.")
            return redirect("users:login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

# 🔹 Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}! 👋")
                next_url = request.GET.get("next", "blog:home")  # keep ?next
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login details. Try again.")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


# 🔹 Logout View
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("blog:home")

# @login_required
# def profile(request):
#     if request.method == "POST":
#         form = UserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your profile was updated successfully!")
#             return redirect("users:profile")
#     else:
#         form = UserChangeForm(instance=request.user)

#     return render(request, "users/profile.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Your profile has been updated successfully!")
            return redirect("users:profile")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "users/profile.html", {
        "form": form,
        "user_obj": request.user,   # 👈 send user separately for clarity
    })