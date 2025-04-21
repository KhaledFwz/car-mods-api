from django.contrib import admin
from .models import CarBrand,CarModel,Modification,ModificationShop
# Register your models here.

#CarBrand admin
@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display=('name',)

#CarModel admin 
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display=('name', 'brand')
    list_filter= ('brand',)



#Modification admin
@admin.register(Modification)
class ModificationAdmin(admin.ModelAdmin):
    list_display=('title','model')
    list_filter= ('model',)


#ModificationShop admin
@admin.register(ModificationShop)
class ModificationShopAdmin(admin.ModelAdmin):
    list_display=('name','address','phone')
    filter_horizontal = ('services',)
