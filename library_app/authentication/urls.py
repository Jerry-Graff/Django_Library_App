from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="authentication/login.html"),
        name="login"),

    path(
        "logout/",
        views.logout_user,
        name="logout"),

    path("register/", views.register_user, name="register"),
]
