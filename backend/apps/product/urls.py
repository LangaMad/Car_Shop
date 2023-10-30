from django.urls import path

from .views import *

urlpatterns = [
    path('',ProductView.as_view(),name = 'index'),
    path('detail/<int:pk>/',DetailCarView.as_view(),name = 'car_detail'),
    path('cars/list/',CarAllAPIview.as_view({'get':'list'})),
    path('cars/detail/<int:pk>/',CarAllAPIview.as_view({'put':'update'})),
    # path('car/list/',CarListAPIview.as_view()),
    # path('car/create/',CarCreateAPIview.as_view()),
    # path('car/image/',CarImageAPIview.as_view()),
    # path('car/createimage/',CarImageCreateAPIview.as_view()),
    # path('car/update/<int:pk>/',CarUpdateAPIview.as_view()),
    # path('car/delete/<int:pk>/',CarDeleteAPIview.as_view()),
    # path('car/detail/<int:pk>/',CarDetailAPIview.as_view()),


]