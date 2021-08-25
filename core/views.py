from django.shortcuts import render


def homeview(request):
    return render(request, "core/home.html")
