from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import AdvertisementSerializer
from .models import AdvertisementModel


class AdvertisementAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdvertisementModel.objects.all()
    serializer_class = AdvertisementSerializer