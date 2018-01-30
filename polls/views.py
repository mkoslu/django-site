from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD
from django.http import HttpResponse
=======
>>>>>>> df579e5dc27786635d13f2dcd7fc690b985f823b
=======
from django.http import HttpResponse
>>>>>>> 4e213486b4a26bfc6ae50a195eb61e5d50242ffe

# Create your views here.
def index(request):
    return HttpResponse("hello, world. You're at the polls index.")
