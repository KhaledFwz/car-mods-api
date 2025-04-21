from rest_framework import viewsets
from .models import CarModel,CarBrand,Modification,ModificationShop
from .serializers import CarBrandSerializer,CarModelSerializer,ModificationSerializer,ModificationShopSerializer



# Create your views here.


#CarBrand view
class CarBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarBrand.objects.all() 
    serializer_class = CarBrandSerializer


#CarModel view
class CarModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarModel.objects.all() 
    serializer_class = CarModelSerializer


#Modification view
class ModificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Modification.objects.all()
    serializer_class = ModificationSerializer


#ModificationShop view
class ModificationShopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ModificationShop.objects.all()
    serializer_class = ModificationShopSerializer