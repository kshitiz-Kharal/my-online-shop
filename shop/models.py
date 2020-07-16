from django.db import models

# Create your models here.

from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):
    view_on_site = True


class Product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=70, default="")
    Category = models.CharField(max_length=60,  default="")
    SubCategory = models.CharField(max_length=60,  default="")
    Price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/images', default="")
    Description = models.CharField(max_length=300,  default="")
    Published_date = models.DateField()

    def __str__(self):
        return self.Product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, default="")
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=70, default="")
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=70, default="")
    amount = models.IntegerField(default=0)
    address = models.CharField(max_length=150, default="")
    address2 = models.CharField(max_length=150, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=30)
    zip_code = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    

