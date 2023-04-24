from django.db import models

# Create your models here.
class Form(models.Model):
    name=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    profile_pic=models.FileField(max_length=255,upload_to='media/Images',null=True,default=None)
