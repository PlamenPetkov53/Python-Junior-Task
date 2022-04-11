"""JuniorTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
import AssetManagement.views as asset_views


app_name = 'assets'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asset_views.Home, name="home"),
    path('createbrand', asset_views.create_brand, name='createbrand'),
    path('createmodel', asset_views.create_model, name='createmodel'),
    path('createusercar', asset_views.create_usercar, name='createusercar'),
    #path('delete_brand', asset_views.delete_brand, name='deletebrand')
    re_path(r'^searchuser/$', asset_views.search_user, name='search'),
    re_path(r'^search/$', asset_views.search_user_car, name='searchcar'),
    re_path(r'^searchbrand/$', asset_views.search_car_brand, name='search_brand'),
    re_path(r'^searchmodel/$', asset_views.search_car_model, name='search_model'),
    path('user_cars/delete/<id>', asset_views.delete_user_car, name="delete"),
    path('user_cars/delete/brand/<id>', asset_views.delete_car_brand, name="delete_brand"),
    path('user_cars/delete/model/<id>', asset_views.delete_car_model, name="delete_model"),
    path('user_cars', asset_views.show_user_cars, name='user_cars'),
    path('car_brands', asset_views.show_car_brands, name='car_brands'),
    path('car_models', asset_views.show_car_models, name='car_models'),


]
