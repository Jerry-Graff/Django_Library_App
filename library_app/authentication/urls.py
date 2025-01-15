from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_user

urlpatterns = [
    path(
        "login/",  # Use Djangos built in Login view
        LoginView.as_view(template_name="registration/login.html"),
        name="login"),

    path(
        "logout/",  # Use djangos built in Logout view
        LogoutView.as_view(next_page="login"),  # Redirect user to login
        name="logout"),

    path("register/", register_user, name="register"),
]
