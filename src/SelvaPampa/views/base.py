from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse

# Create your views here.

def base(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse("<h1>Holaaaa</h1>")