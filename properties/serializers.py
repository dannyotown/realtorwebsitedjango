from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields =  ('property_id','address','zip_code','city','state_abbreviation','number_of_bedrooms','number_of_bathrooms','square_feet','price','sold','lease','priority','created_date')