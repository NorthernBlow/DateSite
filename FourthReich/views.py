from django.shortcuts import render
from django.https import HttpResponse

def response(request):
    print(request)
    return HttpResponse('Hello world')

# Create your views here.
