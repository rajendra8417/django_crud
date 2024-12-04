from django.db import models


class student(models.Model):
    #id= models.AutoField()
    name=models.CharField(max_length=15)
    age=models.IntegerField(null=True)
    email=models.EmailField()
    #image=models.ImageField()
    file=models.FileField()


class product(models.Model):
    pass