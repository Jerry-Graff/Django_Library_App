from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<int:pk>/", views.book_detail, name="book_detail"),
    path("create/", views.create_book, name="book_create"),
    path("<int:pk>/update/", views.update_book, name="book_update"),
    path("<int:pk>/delete/", views.delete_book, name="book_delete"),
    path("<int:pk>/assign", views.assign_book, name="assign_book")
]
