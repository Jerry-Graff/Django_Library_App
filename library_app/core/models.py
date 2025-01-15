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
    email = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Username: {self.user}"


class BookLoan(models.Model):
    """
    Track which reader has a book and when it is due back.
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} loaned to {self.reader.user.username}"
