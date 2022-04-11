import re
from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from ManagementRestFramework.views import CarBrandList
from appcore.models import UserCar, CarModel, CarBrand, CustomUser
from .forms import CarBrandCreate, UserCarCreate, CarModelCreate
from django.contrib.auth.decorators import login_required
from .filters import CarBrandFilter, CarModelFiler, UserCarFilter, UserFilter



# Create your views here.
@login_required
def Home(request):
      context = {}
      return render(request, "home.html", context)


def create_brand(request):
      create_brand = CarBrandCreate()
      if request.method == "POST":
            create_brand = CarBrandCreate(request.POST)
            if create_brand.is_valid():
                  create_brand.save()
                  create_brand = CarBrandCreate()
                  context = {'form' : create_brand}
                  return render(request, "create_brand.html", context)
            else:
                  return redirect("assets:createbrand")
      else:
            create_brand = CarBrandCreate()
            context = {'form' : create_brand}
            return render(request, 'create_brand.html', context)


def create_model(request):
      create_model = CarModelCreate()
      if request.method == "POST":
            create_model = CarModelCreate(request.POST)
            if create_model.is_valid():
                  create_model.save()
                  create_model = CarModelCreate()
                  context = {'form' : create_model}
                  return render(request, "create_model.html", context)
            else:
                  return redirect("assets:createmodel")
      else:
            create_model = CarModelCreate()
            context = {'form' : create_model}
            return render(request, 'create_model.html', context)


def create_usercar(request):
      create_usercar = UserCarCreate()
      if request.method == "POST":
            create_usercar = UserCarCreate(request.POST)
            if create_usercar.is_valid():
                  create_usercar.save()
                  create_usercar = UserCarCreate()
                  context = {'form' : create_usercar}
                  return render(request, "create_user_car.html", context)
            else:
                  return redirect("assets:createusercar")
      else:
            create_usercar = UserCarCreate()
            context = {'form' : create_usercar}
            return render(request, 'create_user_car.html', context)



def search_user(request):
      user_list = CustomUser.objects.all()
      user_filter = UserFilter(request.GET, queryset=user_list)
      context = {'user_filter' : user_filter}
      return render(request, 'user_list.html', context)


def search_user_car(request):
      
      car_user_list = UserCar.objects.all()
      user_car_filter = UserCarFilter(request.GET, queryset=car_user_list)
      context = {'car_user_filter' : user_car_filter}
      return  render(request, 'user_list.html', context)

def search_car_brand(request):
      car_brand_list = CarBrand.objects.all()
      car_brand_filter = CarBrandFilter(request.GET, queryset=car_brand_list)
      context = {'car_brand_filter' : car_brand_filter}
      return  render(request, 'user_list.html', context)


def search_car_model(request):
      car_model_list = CarModel.objects.all()
      car_model_filter = CarModelFiler(request.GET, queryset=car_model_list)
      context = {'car_model_filter' : car_model_filter}
      return  render(request, 'user_list.html', context)


def show_user_cars(request):
      data = UserCar.objects.all()
      context = {'data' : data}
      return render(request, 'user_car_table.html', context)


def show_car_brands(request):
      data = CarBrand.objects.all()
      context = {'data' : data}
      return render(request, 'car_brands_table.html', context)


def show_car_models(request):
      data = CarModel.objects.all()
      context = {'data' : data}
      return render(request, 'car_models_table.html', context)


def delete_user_car(request, id):
      user_car = get_object_or_404(UserCar, id=id)
      user_car.isDeleted = True
      user_car.deleted_at = datetime.now()
      user_car.save()
      return redirect('assets:user_cars')


def delete_car_brand(request, id):
      user_car = get_object_or_404(CarBrand, id=id)
      user_car.is_deleted = True
      user_car.deleted_at = datetime.now()
      user_car.save()
      return redirect('assets:car_brands')


def delete_car_model(request, id):
      user_car = get_object_or_404(CarModel, id=id)
      user_car.isDeleted = True
      user_car.update_at = datetime.now()
      user_car.save()
      return redirect('assets:car_models')


