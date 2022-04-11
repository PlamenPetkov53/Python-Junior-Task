from email.policy import default
from statistics import mode
from django.db.models import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    is_visitor = models.BooleanField(default=False)
    is_creator = models.BooleanField(default=False)
    city_birth = models.CharField(max_length=200, blank=True)

    def __str__(self) :
          return self.username


class CarBrand(models.Model):
      brand_name = models.CharField(max_length=255)
      created_at = models.DateTimeField(default=datetime.now)
      deleted_at = models.DateTimeField(default=datetime.now)
      is_deleted = models.BooleanField(default=False)

      def __str__(self) :
          return self.brand_name


class CarModel(models.Model):
      car_brand = models.ForeignKey("CarBrand", on_delete=models.CASCADE)
      model_name = models.CharField(max_length=255)
      created_at = models.DateTimeField(default=datetime.now)
      update_at = models.DateTimeField(default=datetime.now)
      isDeleted = models.BooleanField(default=False)
      def __str__(self) :
          return self.model_name


class UserCar(models.Model):
      user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
      car_brand = models.ForeignKey('CarBrand', on_delete=models.CASCADE)
      car_model = models.ForeignKey('CarModel', on_delete=models.CASCADE)
      first_reg = models.DateTimeField(default=datetime.now)
      odometer = models.PositiveBigIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(999999)])
      created_at = models.DateTimeField(default=datetime.now)
      deleted_at = models.DateTimeField(default=datetime.now)
      isDeleted = models.BooleanField(default=False)



