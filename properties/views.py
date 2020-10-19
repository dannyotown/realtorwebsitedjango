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
    try:
        prop = Property.objects.all()
        serializer = PropertySerializer(prop, many=True)
        return Response(serializer.data)
    except:
        return HttpResponse("Server Error", status=404)


# GET ONE PROPERTY.
@api_view(["GET"])
def propertyOne(request, pk):
    try:
        prop = Property.objects.get(property_id=pk)
        serializer = PropertySerializer(prop, many=False)
        return Response(serializer.data)
    except:
        return HttpResponse("Server Error", status=404)


# # CREATE A PROPERTY.
# @api_view(["POST"])
# @user_passes_test(lambda u: u.is_superuser)
# def propertyCreate(request):
#     try:
#         serializer = PropertySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     except:
#         return HttpResponse("Server Error", status=404)


# # UPDATE A PROPERTY.
# @api_view(["POST"])
# @user_passes_test(lambda u: u.is_superuser)
# def propertyUpdate(request, pk):
#     try:
#         prop = Property.objects.get(property_id=pk)
#         serializer = PropertySerializer(instance=task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#     except:
#         return HttpResponse("Server Error", status=404)


# # DELETE A PROPERTY.
# @api_view(["DELETE"])
# @user_passes_test(lambda u: u.is_superuser)
# def propertyDelete(request, pk):
#     try:
#         prop = Property.objects.get(property_id=pk)
#         prop.delete()
#         return HttpResponse("Property Deleted", status=202)
#     except:
#         return HttpResponse("Server Error", status=404)
