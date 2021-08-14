from django.shortcuts import render
from django.http import HttpResponse


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'error_404.html', data)


def home_page(request):
    # data = {"name": "ThePythonDjango.com"}
    return render(request,'homepage.html')
