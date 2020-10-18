from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import HouseSerializer
from .models import House
# Create your views here.
@api_view(['GET'])
def houseList(request):
    house = House.objects.all()
    serializer = HouseSerializer(house, many=True)
    return Response(serializer.data)