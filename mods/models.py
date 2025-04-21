from django.db import models

# Create your models here.


#1- CarBrand
class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brand_logos/')

    def __str__(self):
        return self.name
    
#2- CarModel
class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand,on_delete=models.CASCADE,related_name='models')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_models/')

    def __str__(self):
        return f"{self.brand.name} - {self.name}"
    
#3- Modification
class Modification(models.Model):
    model = models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='modifications')
    title = models.CharField(max_length=100)
    description = models.TextField()
    before_image = models.ImageField(upload_to='modifications/before/')
    after_image = models.ImageField(upload_to='modifications/after/')

    def __str__(self):
        return self.title
    
#4- ModificationShop
class ModificationShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    location_url = models.URLField()
    phone = models.CharField(max_length=20)
    description = models.TextField()
    services = models.ManyToManyField(Modification,related_name='shops')

    def __str__(self):
        return self.name
