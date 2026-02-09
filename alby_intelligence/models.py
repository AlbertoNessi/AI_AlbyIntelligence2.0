from django.db import models


class Contracts(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)


class Employees(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    address_number = models.CharField(max_length=5)
    birthday = models.DateField("Date of birth")
    place_of_birth = models.CharField(max_length=100)
    fiscal_code = models.CharField(max_length=11)
    contract = models.ForeignKey(Contracts, on_delete=models.CASCADE)
