from rest_framework import serializers
from .models import Allproduct,Expense

class AllproductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Allproduct
        fields =['id','product_name','product_price']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model =Expense
        fields =['id','expense_name','expense_price','expense_officer']