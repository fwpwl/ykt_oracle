from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def test_server(request):
    return HttpResponse("connection success! hello,")

def base_view(request):
    return HttpResponse("welcome success! hello!")
