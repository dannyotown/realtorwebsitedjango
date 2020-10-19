from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PropertySerializer
from .models import Property
from django.contrib.auth.decorators import user_passes_test

# GET ALL PROPERTIES.
@api_view(["GET"])
def propertyList(request):
    prop = Property.objects.all()
    serializer = PropertySerializer(prop, many=True)
    return Response(serializer.data)


# GET ONE PROPERTY.
@api_view(["GET"])
def propertyOne(request, pk):
    prop = Property.objects.get(property_id=pk)
    serializer = PropertySerializer(prop, many=False)
    return Response(serializer.data)


# CREATE A PROPERTY.
@api_view(["POST"])
@user_passes_test(lambda u: u.is_superuser)
def propertyCreate(request):
    serializer = PropertySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return HttpResponse("Property Object is Incorrect", status=400)


# UPDATE A PROPERTY.
@api_view(["POST"])
def propertyUpdate(request, pk):
    prop = Property.objects.get(property_id=pk)
    serializer = PropertySerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return HttpResponse("Property Object is Incorrect", status=400)


# DELETE A PROPERTY.
@api_view(["DELETE"])
def propertyDelete(request, pk):
    prop = Property.objects.get(property_id=pk)
    if prop is not None:
        prop.delete()
        return HttpResponse("Property Deleted", status=202)
    else:
        return HttpResponse("Property Object is Incorrect", status=400)
