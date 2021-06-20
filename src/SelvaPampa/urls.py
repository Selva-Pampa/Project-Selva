from django.contrib import admin
from django.urls import path

from .views import item_list, users, login, item_detail
from .views.item_views import ItemListViews, ItemViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/items/', item_list),
    # path('api/items/<int:id>/', item_detail),
    path('api/items/', ItemListViews.as_view()),
    path('api/items/<int:id>/', ItemViews.as_view()),
    path('api/users/', users),
    path('api/authenticate/', login)
]
