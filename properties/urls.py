from django.urls import path
from . import views

urlpatterns = [
    path("property/", views.propertyList, name="property-list"),
    path("property/<str:pk>", views.propertyOne, name="property-one"),
    # path("property-create/", views.propertyCreate, name="property-create"),
    # path("property-delete/<str:pk>", views.propertyDelete, name="property-delete"),
]
