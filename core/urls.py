from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("intro/", views.intro_view, name="intro"),
    path("greeting/", views.greeting_gview, name="greeting"),
]
