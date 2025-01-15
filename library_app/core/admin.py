from django.contrib import admin
from .models import Book, Reader, BookLoan, Reservation


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_available")


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ("user", "email")


@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ("book", "reader", "loan_date", "due_date")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("book", "reader", "request_date", "is_active")
