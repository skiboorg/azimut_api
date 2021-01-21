from rest_framework import exceptions, serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'





class CarOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarOptions
        fields = '__all__'

class CarImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarImage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    option = CarOptionsSerializer(many=True)
    images = CarImageSerializer(many=True)
    cat_name = serializers.CharField(source='get_cat_name')
    cat_slug = serializers.CharField(source='get_cat_slug')
    class Meta:
        model = Car
        fields = [
            'id',
            'name',
            'name_slug',
            'price_hour',
            'price_km',
            'min_hour',
            'seats',
            'description',
            'option',
            'images',
            'cat_name',
            'cat_slug',

        ]




class AutoSubCategorySerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)
    class Meta:
        model = AutoSubCategory
        fields = '__all__'

class AutoCategorySerializer(serializers.ModelSerializer):
    subcategory = AutoSubCategorySerializer(many=True)
    class Meta:
        model = AutoCategory
        fields = '__all__'