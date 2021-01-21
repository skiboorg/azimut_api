from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *

class GetIndexCars(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.filter(show_at_index=True, is_active=True)


class GetCarsByService(generics.ListAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        service = Service.objects.get(name_slug=self.request.query_params['service_name_slug'])
        return Car.objects.filter(service=service)

class GetIndexServices(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(show_at_index=True)




class GetCar(generics.RetrieveAPIView):
    serializer_class = CarSerializer

    def get_object(self):
        return Car.objects.get(name_slug=self.request.query_params['name_slug'])


class GetCategory(generics.RetrieveAPIView):
    serializer_class = AutoCategorySerializer
    def get_object(self):
        return AutoCategory.objects.get(name_slug=self.request.query_params['name_slug'])

class GetCategories(generics.ListAPIView):
    serializer_class = AutoCategorySerializer
    queryset = AutoCategory.objects.all()

class GetServices(generics.ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

