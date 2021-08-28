from django.shortcuts import render


def home_view(request):
    return render(request, "core/home.html")


def intro_view(request):
    return render(request, "core/intro.html")


def greeting_gview(request):
    return render(request, "core/greeting.html")
