from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200)
    course=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    gender=models.CharField(max_length=100)

    def __str__(self):
        return self.name
