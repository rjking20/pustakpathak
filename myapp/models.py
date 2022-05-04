from django.db import models

# Create your models here.

class Imgstore(models.Model):
    img= models.ImageField(upload_to='pics')
    url= models.CharField(max_length=200)    
    