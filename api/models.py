from django.db import models

# Create your models here.
class Person(models.Model):
    surname = models.CharField(max_length = 50)
    second_surname = models.CharField(max_length=50)
    pre_names = models.CharField(max_length = 50)
    birthdate = models.DateTimeField()
    sex = models.CharField(max_length = 1)
    address = models.CharField(max_length= 150)
    city = models.CharField(max_length= 150)