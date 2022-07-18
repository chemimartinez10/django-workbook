from django.urls import path

from modules.security import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("settings", views.settings, name="settings"),
]
