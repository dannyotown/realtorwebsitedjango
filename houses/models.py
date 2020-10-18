from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=200)
    zip_code = models.IntegerField(validators=[MaxValueValidator(99999),MinValueValidator(10000)])
    city = models.CharField(max_length=100)    
    state_abbreviation = models.CharField(max_length=2)
    number_of_bedrooms = models.IntegerField(validators=[MaxValueValidator(20),MinValueValidator(1)])
    number_of_bathrooms = models.IntegerField(validators=[MaxValueValidator(20),MinValueValidator(1)])
    square_feet = models.IntegerField(validators=[MaxValueValidator(10000),MinValueValidator(1)])
    price = models.IntegerField()
    created_date = models.DateField()

