from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PropertySerializer
from .models import Property
# Create your views here.
@api_view(['GET'])
def propertyList(request):
    prop = Property.objects.all()
    serializer = PropertySerializer(prop, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def propertyOne(request, pk):
    prop = Property.objects.get(property_id=pk)
    serializer = PropertySerializer(prop, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def propertyCreate(request):
    serializer = PropertySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return HttpResponse('Property Object is Incorrect', status=400)