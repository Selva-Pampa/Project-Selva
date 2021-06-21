from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from ..models import Item
from ..serializers import ItemSerializer


class ItemViews(APIView):
    """
        Esta clase permite agrupar todas las vistas
        especificas de un item.
    """
    item = None
    permission_classes = [permissions.IsAuthenticated]

    def dispatch(self, request, *args, **kwargs):
        try:
            self.item = Item.objects.get(id=kwargs.get('id'))
        except Item.DoesNotExist:
            return HttpResponse(status=404)

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id):
        serializer = ItemSerializer(self.item)
        return Response(serializer.data)

    def put(self, request, id):
        serializer = ItemSerializer(self.item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        self.item.delete()
        return HttpResponse(status=204)


class ItemListViews(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
