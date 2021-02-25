from django.urls import path
from . import views

urlpatterns = [



    path('get_services', views.GetServices.as_view()),
    path('get_index_services', views.GetIndexServices.as_view()),
    path('get_index_cars', views.GetIndexCars.as_view()),

    path('get_cars_by_service', views.GetCarsByService.as_view()),
    path('get_categories', views.GetCategories.as_view()),
    path('get_category', views.GetCategory.as_view()),
    path('get_car', views.GetCar.as_view()),


]
