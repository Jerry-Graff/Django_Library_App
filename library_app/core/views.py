from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Book, Reader, BookLoan, Reservation
from .forms import BookForm


@login_required
def book_list(request):
    """ Lists all books """
    books = Book.objects.all()
    return render(request, "core/book_list.html", {"books": books})


@login_required
def book_detail(request, pk):
    """ Display details of a single book """
    book = get_object_or_404(Book, pk=pk)
    return render(request, "core/book_details.html", {"book": book})


@user_passes_test(lambda u: u.is_staff)
def create_book(request):
    """ Admin-only: Add a new book to the list """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:book_list")
    else:
        form = BookForm()
    return render(request, "core/book_form.html", {"form": form})


@user_passes_test(lambda u: u.is_staff)
def update_book(request, pk):
    """ Admin-only: Update an existing book """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("core:book_detail", pk=pk)
    else:
        form = BookForm(instance=book)
    return render(request, "core/book_form.html", {"form": form})


@user_passes_test(lambda u: u.is_staff)
def delete_book(request, pk):
    """ Admin-only: Delete a book """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("core:book_list")
    return render(request, "core/book_confirm_delete.html", {"book": book})


@login_required
def assign_book(request, pk):
    """ Loan a book to the current user (Reader) """
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # Ensure user profile exsists if not make one
        reader, created = Reader.objects.get_or_create(user=request.user)
        BookLoan.objects.create(book=book, reader=reader)
        book.is_available = False
        book.save()
        return redirect("core:book_detail", pk=book.pk)
    return render(request, "core/assign_book.html", {"book": book})


@login_required
def reserve_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.is_available:
        messages.error(request, "This book is currently available")
        return redirect("core:book_detail", pk=book.pk)
    if Reservation.objects.filter(book=book, is_active=True).exclude(reader__user=request.user).exists():
        messages.error(request, "This book is already reserved by someone else.")
        return redirect("core:book_detail", pk=book.pk)
    reader, _ = Reader.objects.get_or_create(user=request.user)
    Reservation.objects.create(book=book, reader=reader)
    messages.success(request, "You have reserved this book successfully.")
    return redirect("core:book_detail", pk=book.pk)


@user_passes_test(lambda u: u.is_staff)
def reader_list(request):
    """ Admin-only: List all readers """
    readers = Reader.objects.select_related('user')
    return render(request, "core/reader_list.html", {"readers": readers})


@user_passes_test(lambda u: u.is_staff)
def reader_detail(request, reader_id):
    """ Admin-only: Show reader details and borrowed books """
    reader = get_object_or_404(Reader, pk=reader_id)
    return render(request, "core/reader_detail.html", {"reader": reader})
