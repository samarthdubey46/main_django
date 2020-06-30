from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    profice_pic = models.ImageField(null=True,default='profile1.png',blank=True)

    def __str__(self):
        return str(self.name)



class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    choices = (
        ('Outdoor', "Outdoor"),
        ('Indoor', "Indoor"),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=20000, null=True)
    category = models.CharField(max_length=200, null=True, choices=choices)
    description = models.CharField(max_length=200, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name


class Order(models.Model):
    choice = (
        ('Pending', "Pending"),
        ('Shipped', "Shipped"),
        ("Delivered", "Delivered")
    )
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=choice)
    date_created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.Product.name

# Create your models here.
