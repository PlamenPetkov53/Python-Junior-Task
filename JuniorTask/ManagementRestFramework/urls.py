from django.contrib import admin
from django.urls import path
import ManagementRestFramework.views as managers_views



app_name = 'manager_rest_framework'

urlpatterns = [
    path('', managers_views.ApiOverview, name='home'),
    path('create/', managers_views.add_usercar, name='add_user_car'),
    path('all/', managers_views.view_all, name='view_all'),
    path('all/usercars', managers_views.UserCarList.as_view(), name='view_user_car'),
    path('all/models', managers_views.CarModelList.as_view(), name='view_car_models'),
    path('all/brands', managers_views.CarBrandList.as_view(), name='view_car_brands'),
    path('delete/<int:pk>/', managers_views.delete_user_car, name='update_items'),
    path('delete/model/<int:pk>/', managers_views.delete_model, name='car_model_delete'),
    path('delete/brand/<int:pk>/', managers_views.delete_brand, name='car_brand_delete'),
    path('create/brand', managers_views.add_brand, name='add_car_brand'),
    path('create/model', managers_views.add_model, name='add_car_model'),




]