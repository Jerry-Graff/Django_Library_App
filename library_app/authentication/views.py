from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register_user(request):
    """
    
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core/book_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
