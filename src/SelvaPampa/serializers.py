from rest_framework import serializers

from .models.item import *
from .models.design import *
from .models.substratum import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = '__all__'


class SubstratumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Substratum
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'designs']
