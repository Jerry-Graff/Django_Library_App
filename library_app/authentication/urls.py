from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path(
        "login/",  # Use Djangos built in Login view
        LoginView.as_view(template_name="authentication/login.html"),
        name="login"),

    path(
        "logout/",  # Use djangos built in Logout view
        views.logout_user,  # Redirect user to login
        name="logout"),

    path("register/", views.register_user, name="register"),
]
