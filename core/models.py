from django.db import models


# Create your models here.
class Department(models.Model):
    department_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_id


class Employee(models.Model):
    STATUS = (
        ('m', 'Married'),
        ('s', 'Single'),
        ('n', 'None')
    )
    EMP_STATUS = (
        ('p', 'Permanent'),
        ('c', 'Contractual')
    )
    employee_id = models.CharField(max_length=10, unique=True)
    d_o_b = models.DateField(verbose_name='Date of Birth')
    nationality = models.CharField(max_length=100)
    employment = models.DateField(verbose_name='Date of Employment')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, verbose_name='Mobile Phone')
    status = models.CharField(max_length=1, choices=STATUS, verbose_name='Marital Status')
    emp_status = models.CharField(verbose_name='Employment', max_length=1, choices=EMP_STATUS)

    def __str__(self):
        return self.employee_id


class EmployeeEducation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    level = models.CharField(max_length=200)
    grade = models.CharField(max_length=2)
    major = models.CharField(max_length=200)

    def __str__(self):
        return str(self.employee)
