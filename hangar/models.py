from django.db import models

# Create your models here.
class Feature(models.Model):
 
    image = models.ImageField(null=True,default=None)
    type=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.name
    
class Latest(models.Model):
    image = models.ImageField(null=True,default=None)
    type=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.name