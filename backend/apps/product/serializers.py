from rest_framework import serializers
from .models import Car,CarImage

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"
        read_only_fields = ["id"]


class CarImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarImage
        fields = "__all__"
        read_only_fields = ["id"]



