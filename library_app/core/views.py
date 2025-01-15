from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Book
from .forms import BookForm


def book_list(request):
    """
    Lists all books
    """
    books = Book.objects.all()
    return render(request, "core/book_list.html", {"books": books})


def book_detail(request, pk):
    """
    List specific book details
    """
    book = get_object_or_404(Book, pk=pk)
    return render(request, "core/book_details.html", {"book": book})


def create_book(request):
    """
    Add a new book to book list
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("core/book_list.html"))
        else:
            form = BookForm()
            return render(request, "core/book_form.html", {"form": form})


def update_book(request, pk):
    """
    Update an exsisting title in the book list
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse("core/book_details", args=[pk]))
        else:
            form = BookForm(instance=book)
    return render(request, "core/book_form.html", {"form": form})


def delete_book(request, pk):
    """
    Delete a book from book list
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect(reverse("core/book_list.html"))
    return render(request, "core/book_confirm_delete.html", {"book": book})
