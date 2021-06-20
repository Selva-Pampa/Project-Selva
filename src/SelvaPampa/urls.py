from django.contrib import admin
from django.urls import path
from .views.base import item_list, users, login, item_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/', item_list),
    path('api/items/<int:id>/', item_detail),
    path('api/users/', users),
    path('api/authenticate/', login)
]
