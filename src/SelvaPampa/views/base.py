import re
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser

from ..models import Item
from ..serializers import DesignSerializer, ItemSerializer, SubstratumSerializer


def item_list(request: HttpRequest):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.POST:
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    # se podria agregar un PUT para actualizar Items


def item_detail(request: HttpRequest, id: int):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)


def users(request: HttpRequest):
    if request.POST:
        body = request.POST  # Esto se llena en el front
        if 'username' in body.keys():
            user = User.objects.create_user(
                body.get('username'), body.get('email'), body.get('password'))
        # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword', **extraFields)


def login(request: HttpRequest):
    if request.POST:
        body = request.POST
        user = authenticate(username=body.get('username'),
                            password=body.get('password'))
        if user:
            l(request, user)
