from django import forms
from appcore.models import UserCar, CarBrand, CarModel

class UserCarCreate(forms.ModelForm):
      class Meta:
            model = UserCar
            fields = '__all__'

class CarBrandCreate(forms.ModelForm):
      class Meta:
            model = CarBrand
            fields = ['brand_name', 'created_at'] #TODO: Delete deleted_at default date!!!!


class CarModelCreate(forms.ModelForm):
      class Meta:
            model = CarModel
            fields = '__all__'