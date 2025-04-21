from rest_framework import serializers
from .models import CarBrand,CarModel,Modification,ModificationShop


#CarBrand serializer
class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'



#CarModel serializer
class CarModelSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer(read_only=True)
    class Meta:
        model = CarModel
        fields = '__all__'


#Modification serializer
class ModificationSerializer(serializers.ModelSerializer):
    model = CarModelSerializer(read_only=True)
    
    class Meta:
        model = Modification
        fields = '__all__'


#ModificationShop serializer
class ModificationShopSerializer(serializers.ModelSerializer):
    services = ModificationSerializer(many=True,read_only=True)


    class Meta:
        model = ModificationShop
        fields = '__all__'