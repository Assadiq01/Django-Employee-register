from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name