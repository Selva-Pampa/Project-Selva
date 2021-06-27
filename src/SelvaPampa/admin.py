from django.contrib import admin
from .models.design import Design
from .models.substratum import Substratum
from .models.item import Item

# admin.site.register(User)
admin.site.register(Design)
admin.site.register(Substratum)
admin.site.register(Item)
