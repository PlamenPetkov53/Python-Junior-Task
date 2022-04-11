from django.forms import ValidationError
from django.shortcuts import render, get_object_or_404
from ManagementRestFramework import serlializers
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from appcore.models import CustomUser, CarBrand, CarModel, UserCar
from ManagementRestFramework.serlializers import UserCarSerializer, CarBrandSerializer, CarModelSerializer
from rest_framework import serializers
from rest_framework import status
from datetime import datetime
from django.http import request, response


# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
      api_urls = {
        'all_items': '/all',
        'View Car Brands': '/all/brands',
        'View Car Models': '/all/models',
        'View User Cars': '/all/usercars',
        'Add Car to User': '/create',
        'Add Car Brand': '/create/brand',
        'Add Car Model': '/create/model',
        'Delete User Car': '/delete/<int:pk>',
        'Delete Car Brand': '/delete/brand/<int:pk>',
        'Delete Car Model': '/delete/model/<int:pk>',
      }
        
      user_car = {        
        'Format for User Car' : "Time by default is se to datetime.now() and isDeleted is False",
        "first_reg": "",
        "odometer": "",
        "created_at": "",
        "deleted_at": "",
        "isDeleted": "False",
        "user": "<int:id>",
        "car_brand": "<int:id>",
        "car_model": "<int:id>"
        }

      car_brand = {
        'Format for Car Brand' : "Time by default is se to datetime.now() and isDeleted is False",
        "brand_name": "",
        "created_at": "",
        "deleted_at": "",
        "is_deleted": "False"
      }

      car_model = {
        "car_brand": "<int:id>",
        "model_name": "",
        "created_at": "",
        "update_at": "",
        "isDeleted": "False"
      }

      return Response({'Api URLS' : api_urls, 'Model_Helper' : [user_car, car_brand, car_model]})



@api_view(['POST'])
def add_usercar(request):
    user_car = UserCarSerializer(data=request.data)

    if UserCar.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This Car already exists')
        
    if user_car.is_valid():
     
        user_car.save()
        return Response(user_car.data)
    else:    
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def add_brand(request):
    car_brand = CarBrandSerializer(data=request.data)

    if CarBrand.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This Brand Already Exists')

    if car_brand.is_valid():

        car_brand.save()
        return Response(car_brand.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['POST'])
def add_model(request):

    car_model = CarModelSerializer(data=request.data)
        
    if CarModel.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This Car Model Already Exists')

    if car_model.is_valid():
            
        car_model.save()
        return Response(car_model.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
   



@api_view(['GET'])
def view_all(request):
   
    if request.query_params:
         user_cars = UserCar.objects.filter(**request.query_param.dict())
         car_brand = CarBrand.objects.filter(**request.query_param.dict())
         car_model = CarModel.objects.filter(**request.query_param.dict())

    else:
        user_cars = UserCar.objects.all()
        car_brand = CarBrand.objects.all()
        car_model = CarModel.objects.all()
    
  
    
    if user_cars or car_brand or car_model:
        user_car_serializer = UserCarSerializer(user_cars, many=True)
        brand_serializer = CarBrandSerializer(car_brand, many=True)
        car_model_serializer = CarModelSerializer(car_model, many=True)
        return Response({'User Car Model' : user_car_serializer.data, 'Car Brand Model' : brand_serializer.data, 'Car Model' : car_model_serializer.data})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class UserCarList(generics.ListAPIView):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer

    filterset_fields = '__all__'

    @api_view(['GET'])
    def view_user_car(request):
        if request.query_params:
            user_cars = UserCar.objects.filter(**request.query_param.dict())
        else:
            user_cars = UserCar.objects.all()

        if user_cars:
            user_car_serializer = UserCarSerializer(user_cars, many=True)
            return Response({'User Car Model' : user_car_serializer.data})


class CarBrandList(generics.ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    
    filterset_fields = '__all__'

    @api_view(['GET'])
    def view_car_brands(request):
        if request.query_params:
            car_brand = CarBrand.objects.filter(**request.query_param.dict())
        else:
            car_brand = CarBrand.objects.all()

        if car_brand:
            car_brand_serializer = CarBrandSerializer(car_brand, many=True)
            return Response({'Car Brands' : car_brand_serializer.data})


class CarModelList(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    
    filterset_fields = '__all__'

    @api_view(['GET'])
    def view_car_models(request):
        if request.query_params:
            car_model = CarModel.objects.filter(**request.query_param.dict())
        else:
            car_model = CarModel.objects.all()

        if car_model:
            car_model_serializer = CarModelSerializer(car_model, many=True)
            return Response({'Car Models' : car_model_serializer.data})



@api_view(['DELETE'])
def delete_user_car(request, pk):
    if UserCar.objects.filter(pk=pk):
        item = get_object_or_404(UserCar, pk=pk)
        item.isDeleted = True
        item.deleted_at = datetime.now()
        item.save()
        return Response({
            f'User {item.user} successfully removed his/her car: Brand : {item.car_brand} ---- Model : {item.car_model} ---- Car First Registration {item.first_reg} ---- Odometer : {item.odometer} ' : 'HTTP Status:' + str(status.HTTP_202_ACCEPTED)
            
        })
    else:
        return Response({'Invalid Car User id, please check input!' : 'HTTP Status' + str(status.HTTP_404_NOT_FOUND)})



@api_view(['DELETE'])
def delete_model(request, pk):
    if CarModel.objects.filter(pk=pk):

        item = get_object_or_404(CarModel, pk=pk)
        item.isDeleted = True
        item.update_at = datetime.now()
        item.save()
        return Response({

            f'Model {item.model_name} and  id:{pk} is successfully removed' : 'HTTP Status:' + str(status.HTTP_202_ACCEPTED)
            
            })
    else:
        return Response({'Invalid Car Model id, please check input!' : 'HTTP Status' + str(status.HTTP_404_NOT_FOUND)})



@api_view(['DELETE'])
def delete_brand(request, pk):
    if CarBrand.objects.filter(pk=pk):
        item = get_object_or_404(CarBrand, pk=pk)
        item.is_deleted = True
        item.deleted_at = datetime.now()
        item.save()
        return Response({

            f'Brand {item.brand_name} and  id:{pk} is successfully removed' : 'HTTP Status:' + str(status.HTTP_202_ACCEPTED)
            
            })
    else:
        return Response({'Invalid Brand id, please check input!' : 'HTTP Status' + str(status.HTTP_404_NOT_FOUND)})