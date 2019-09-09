from django.db import models

# Create your models here.

property_type ={
    ("s","small"),
    ("m","medium"),
    ("b","big"),
}


class Property(models.Model):
    name =models.CharField(max_length= 50)
    property_type =models.CharField(choices=property_type,max_length=20)
    price =models.PositiveIntegerField()
    image =models.ImageField(upload_to='property/',null=True)
    def __str__(self):
        return self.name
