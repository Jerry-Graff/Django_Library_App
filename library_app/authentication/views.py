from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ReaderSignUpForm


def register_user(request):
    """
    Basic user signup custom view with email field
    """
    if request.method == "POST":
        form = ReaderSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core/book_list")
    else:
        form = ReaderSignUpForm()
    return render(request, "authentication/register.html", {"form": form})
