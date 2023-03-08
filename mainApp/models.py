from django.db import models
from django.contrib.auth.models import User

class Catergory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    productName = models.CharField(max_length=150,blank=False,null=False)
    productPrice = models.IntegerField(blank=False,null=False)
    productCategory = models.ForeignKey(Catergory,on_delete=models.CASCADE)
    productDesc = models.TextField()
    productImage = models.ImageField(upload_to='media')
    quantityAvailable = models.IntegerField(blank=False,null=False)

    def __str__(self):
        return self.productName

class Cart(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)




