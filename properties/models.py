from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Property(models.Model):
    property_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1500, default='')
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
    photo1 = models.FileField(default='',)
    photo2 = models.FileField(default='',blank=True)
    photo3 = models.FileField(default='',blank=True)
    photo4 = models.FileField(default='',blank=True)
    photo5 = models.FileField(default='',blank=True)
    photo6 = models.FileField(default='',blank=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.address