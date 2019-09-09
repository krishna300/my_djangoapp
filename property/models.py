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

    category =models.ForeignKey('Category',null =True, on_delete=models.SET_NULL)
    image =models.ImageField(upload_to='property/',null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name ='Property'
        verbose_name_plural = 'Properties'

class Category(models.Model):
    category_name =models.CharField(max_length=40)


    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name ='Category'
        verbose_name_plural = 'Categories'


