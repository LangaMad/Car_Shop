from django.shortcuts import render
from .models import Car
from django.views.generic import TemplateView
from django_filters.views import FilterView
from .filters import CarFilter
# Create your views here.

class ProductView(FilterView):
    model = Car
    template_name = 'index.html'
    filterset_class = CarFilter