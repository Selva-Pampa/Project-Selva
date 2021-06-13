from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as l
from django.contrib.auth.decorators import login_required
from SelvaPampa.models.item import Item

def all_items(request : HttpRequest):
    if request.method == 'GET':
        items = list(Item.objects.all())
        return HttpResponse(items)

def users(request : HttpRequest):
    if request.POST:
        body = request.POST # Esto se llena en el front
        if 'username' in body.keys():
            user = User.objects.create_user(body.get('username'),body.get('email'),body.get('password'))
        # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword', **extraFields)

def login(request : HttpRequest):
    if request.POST:
        body = request.POST
        user = authenticate(username=body.get('username'), password=body.get('password'))
        if user:
            l(request,user)
