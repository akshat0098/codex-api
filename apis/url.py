from django.urls import path,include
from .views import *

urlpatterns = [

    path('entry/',TemperatureLogView.as_view(),name="questions_api"),
]
