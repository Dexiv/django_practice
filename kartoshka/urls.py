from django.urls import path
from . import views

urlpatterns = [
    path('kartoshka/', views.vivod_price_potatoes, name='price'),
]