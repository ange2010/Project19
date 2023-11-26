from rest_framework import serializers
from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Item
        fields = ('category', 'name', 'description')

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'
