from django.contrib import admin
from django.urls import path, include

from .views import ItemListViews, ItemViews, UserList, UserDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/', ItemListViews.as_view()),
    path('api/items/<int:id>/', ItemViews.as_view()),
    path('api/users/', UserList.as_view()),
    path('api/users/<int:pk>/', UserDetail.as_view())
]
# TODO: Agregar vistas de designs, substratums

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
