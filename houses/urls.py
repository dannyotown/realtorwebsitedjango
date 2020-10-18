from django.urls import path
from . import views

urlpatterns = [
    path('house',views.houseList, name='house-list'),
]