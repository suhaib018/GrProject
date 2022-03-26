from django.db import models

# Create your models here.

class Faculty(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Department(models.Model):
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    department_employees=models.ForeignKey(Department,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
