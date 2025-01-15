from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # Book list & detail
    path("", views.book_list, name="book_list"),
    path("<int:pk>/", views.book_detail, name="book_detail"),

    # CRUD for books (admin/staff only)
    path("create/", views.create_book, name="book_create"),
    path("<int:pk>/update/", views.update_book, name="book_update"),
    path("<int:pk>/delete/", views.delete_book, name="book_delete"),

    # Assign book
    path("<int:pk>/assign/", views.assign_book, name="assign_book"),

    # reserve book
    path("<int:pk>/reserve/", views.reserve_book, name="reserve_book"),

    # Readers (admin/staff only)
    path("readers/", views.reader_list, name="reader_list"),
    path("readers/<int:reader_id>/", views.reader_detail, name="reader_detail"),
]
