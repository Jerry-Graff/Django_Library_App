from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """
    Keeps track of books in library.
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(max_length=900)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author}"


class Reader(models.Model):
    """
    Stores reader details.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"Username: {self.user}"


class BookLoan(models.Model):
    """
    Track which reader has a book and when it is due back.
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Function to set due date to two weeks after a book is checked out
        """
        if not self.id:
            self.due_date = timezone.now().date() + timedelta(weeks=2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.book.title} loaned to {self.reader.user.username}"


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Reservation for {self.book.title} by {self.reader}"
