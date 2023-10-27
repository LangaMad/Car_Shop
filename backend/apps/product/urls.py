from django.urls import path

from .views import *

urlpatterns = [
    path('',ProductView.as_view(),name = 'index'),
    path('detail/<int:pk>/',DetailCarView.as_view(),name = 'car_detail')

]