from django.db import models


# Create your models here.
class Departments(models.Model):
    department_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_id
