from django.db import models
from django.core.validators import MaxLengthValidator , MinLengthValidator

# Create your models here.
CATEGORY_CHOICES=(
    ('tw','topWear'),
    ('bw','bottomWear'),
    ('m','Mobail'),
    ('l','laptop')
)

class Product(models.Model):
    title= models.CharField( max_length=50)
    des= models.TextField()
    price= models.FloatField()
    discount_price= models.FloatField()
    brand= models.CharField( max_length=50)
    image=models.ImageField(upload_to='images')
    category= models.CharField(choices=CATEGORY_CHOICES, max_length=2)