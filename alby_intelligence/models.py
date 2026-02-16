from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = models.CharField(max_length=100, null=False, unique=True)
    enabled = models.BooleanField()
    deleted_at = models.DateField(null=True)


class Files(models.Model):
    name = models.CharField(max_length=100)
    path = models.TextField()
    upload_date = models.DateTimeField(null=False)
    uploaded_by = models.ForeignKey(Users, on_delete=models.CASCADE)


class CCNL(models.Model):
    name = models.CharField(max_length=100)
    ral = models.IntegerField(null=True)
    file = models.ForeignKey(Files, on_delete=models.CASCADE)


class ContractTypes(models.Model):
    name = models.CharField(max_length=100)


class Contracts(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    file = models.ForeignKey(Files, on_delete=models.CASCADE)
    signed_by_company = models.BooleanField()
    signed_by_employee = models.BooleanField()
    signed_by_company_date = models.DateTimeField()
    signed_by_employee_date = models.DateTimeField()
    ccnl = models.ForeignKey(CCNL, null=True, on_delete=models.SET_NULL)
    validity_start = models.DateField()
    validity_end = models.DateField()
    type = models.ForeignKey(ContractTypes, on_delete=models.RESTRICT)


class Roles(models.Model):
    description = models.CharField(max_length=100)


class Section(models.Model):
    name = models.CharField(max_length=100, null=False)
    navbar_position = models.IntegerField(null=False)


class RoleSections(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)


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
