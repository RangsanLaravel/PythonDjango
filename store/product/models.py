from django.db import models

# Create your models here.
class  Allproduct(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name + '-' + self.product_price

class Expense(models.Model):
    expense_name = models.CharField(max_length=200)
    expense_price = models.CharField(max_length=200)
    expense_officer = models.CharField(max_length=200)

    def __str__(self):
        return self.expense_name

class Contractus(models.Model):
    name =models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    subject =models.CharField(max_length=200)
    message =models.TextField(max_length=500)

    def __str__(self):
        return self.subject
