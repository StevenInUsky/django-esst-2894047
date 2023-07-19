from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello, world!')


def home2(request):
    return HttpResponse('Hello, world2!')