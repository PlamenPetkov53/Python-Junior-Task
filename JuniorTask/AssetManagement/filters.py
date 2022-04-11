import django
from appcore.models import CustomUser, CarBrand, CarModel, UserCar
import django_filters

class UserFilter(django_filters.FilterSet):
      class Meta:
            model = CustomUser
            fields = ['username', 'first_name', 'last_name']


class UserCarFilter(django_filters.FilterSet):
      class Meta:
            model = UserCar
            fields = '__all__'


class CarBrandFilter(django_filters.FilterSet):
      class Meta:
            model = CarBrand
            fields = '__all__'


class CarModelFiler(django_filters.FilterSet):
      class Meta:
            model = CarModel
            fields = '__all__'
