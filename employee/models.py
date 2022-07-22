from django.db import models
from department.models import Department

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    department = models.ForeignKey(to= Department, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name