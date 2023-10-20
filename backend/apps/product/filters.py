import django_filters
from .models import Car
from django import forms

class CarFilter(django_filters.FilterSet):
    transmission = django_filters.ModelChoiceFilter(
        field_name="transmission",
        queryset=Car.objects.all(),
        widget=forms.Select()
    )
    age = django_filters.NumberFilter(
        field_name='age'
    )

    class Meta:
        model = Car
        fields = [
            'transmission',
            'age',
            ]