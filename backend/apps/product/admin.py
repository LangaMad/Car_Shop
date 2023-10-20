from django.contrib import admin
from .models import Car,CarImage

# Register your models here.

@admin.register(CarImage)
class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        'car',
        'photo'
    ]
@admin.register(Car)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'age',
        # 'photo',
        'color',
        'transmission',
        'price',
        'engine',
        'volume',
        'vile_side',
        'mileage',
        'condition'

    ]






