from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    zip_code = models.IntegerField(
        validators=[MaxValueValidator(99999), MinValueValidator(10000)]
    )
    city = models.CharField(max_length=100)
    state_abbreviation = models.CharField(max_length=2)
    number_of_bedrooms = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    square_feet = models.IntegerField()
    price = models.IntegerField()
    sold = models.BooleanField(null=False, default=False)
    lease = models.BooleanField(null=False, default=False)
    priority = models.IntegerField(default=1)
    lat = models.FloatField(default=1)
    long = models.FloatField(default=1)
    created_date = models.DateTimeField(auto_now=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True)
    photos = models.FileField(default='')
    deleted = models.BooleanField(default=False)
