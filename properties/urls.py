from django.urls import path
from . import views

urlpatterns = [
    path("property/", views.getPropertyList, name="property-list"),
    path("property/<str:pk>", views.getProperty, name="property-list"),
]
