from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

try:
    from ..models import Item
except:
    from .models import Item
from ..serializers import ItemSerializer


class ItemViews(APIView):
    """
        Esta clase permite agrupar todas las vistas
        especificas de un item.
    """
    item = None

    def dispatch(self, request: HttpRequest, *args, **kwargs):
        try:
            self.item = Item.objects.get(id=kwargs.get('id'))
        except Item.DoesNotExist:
            return HttpResponse(status=404)

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        serializer = ItemSerializer(self.item)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, id):
        data = JSONParser().parse(request)
        serializer = ItemSerializer(self.item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id):
        self.item.delete()
        return HttpResponse(status=204)


class ItemListViews(APIView):

    def get(self, request: HttpRequest):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request: HttpRequest):
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
