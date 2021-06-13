from django.contrib import admin
from django.urls import path
from SelvaPampa.views.base import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/',all_items),
    path('users/',users),
    path('authenticate/',login)
]
