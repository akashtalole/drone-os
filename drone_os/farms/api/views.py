from rest_framework import generics
from rest_framework import viewsets
from ..models import Farm
from ..serializers import FarmSerializer

#class FarmList(generics.ListCreateAPIView):
class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer