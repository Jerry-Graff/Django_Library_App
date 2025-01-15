from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("books/<int:pk>/", views.book_detail, name="book_details"),
    path("books/create/", views.create_book, name="book_create"),
    path("books/<int:pk>/update/", views.update_book, name="book_update"),
    path("books/<int:pk>/delete/", views.delete_book, name="book_delete")
]
