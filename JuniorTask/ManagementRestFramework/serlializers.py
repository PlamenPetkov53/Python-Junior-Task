from django.db.models import fields
from rest_framework import serializers
from appcore.models import CustomUser, UserCar, CarModel, CarBrand

class UserCarSerializer(serializers.ModelSerializer):
      #user = serializers.StringRelatedField()
      #car_brand = serializers.StringRelatedField()
      #car_model = serializers.StringRelatedField()

      class Meta:
            model = UserCar
            fields = '__all__'

class CarModelSerializer(serializers.ModelSerializer):
      #car_brand = serializers.IntRelatedField()

      class Meta: 
            model = CarModel
            fields = '__all__'


class CarBrandSerializer(serializers.ModelSerializer):
      class Meta:
            model = CarBrand
            fields = '__all__'