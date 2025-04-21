from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CarBrandViewSet,CarModelViewSet,ModificationViewSet,ModificationShopViewSet




routers = DefaultRouter()
#Brands 
routers.register('brands',CarBrandViewSet)

#Models 
routers.register('models',CarModelViewSet)

#Modifications
routers.register('modifications', ModificationViewSet)

#ModificationShop 
routers.register('shops',ModificationShopViewSet)


urlpatterns = [
    path('',include(routers.urls)),
]