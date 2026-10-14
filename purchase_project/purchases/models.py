from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile', null=True)
    full_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=200, null=True)
    picture = models.ImageField(upload_to='media/profile_img', blank=True, null=True)

    def __str__(self):
        return f'{self.full_name}'


class SupplierModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplier_profile', null=True)
    supplier_name = models.CharField(max_length=200, null=True)  
    contact_number = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)  

    def __str__(self):
            return f'{self.supplier_name}'

class PurchaseRecordModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True)
    supplier_name = models.ForeignKey(SupplierModel, on_delete=models.CASCADE, related_name='supplier', null=True)
    supplier =  models.CharField(max_length=200, null=True)
    product_name = models.CharField(max_length=200, null=True)
    quantity = models.FloatField(null=True)
    unit_price = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    paid_amount = models.FloatField(null=True)
    purchase_date = models.DateField(null=True)

    def __str__(self):
                return f'{self.product_name}'