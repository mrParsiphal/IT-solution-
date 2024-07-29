from rest_framework import serializers
from .models import AdvertisementModel


class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvertisementModel
        fields = '__all__'
