from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import contractform

############# API ###################
from django.http import JsonResponse
from .serializer import AllproductSerializer, ExpenseSerializer
from .models import Allproduct, Expense

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
#####################################


# Create your views here.
def Home(request):
    # return HttpResponse('<h1>Hello world</h1>')
    return render(request, 'product/home.html')


def About(request):
    return render(request, 'product/about.html')


def APIAllproduct(request):
    allproduct = Allproduct.objects.all()  # การ filter [:2]
    print(allproduct)
    # ต้องใส่เข้าไปทุกครั้งเพื่อ serial
    serializer = AllproductSerializer(allproduct, many=True)
    print(serializer)
    print(serializer.data)
    # ภาษาไทย
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def APIProduct(request, pk):
    singleproduct = Allproduct.objects.get(id=pk)  # ดึงค่าจาก PK
    # ต้องใส่เข้าไปทุกครั้งเพื่อ serial
    serializer = AllproductSerializer(singleproduct)
    # ภาษาไทย json_dumps_params={'ensure_ascii':False}
    return JsonResponse(serializer.data, safe=True, json_dumps_params={'ensure_ascii': False})


@api_view(['POST'])
def api_post_allproduct(request):
    allproduct = Allproduct()
    if request.method == 'POST':
        serializer = AllproductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)


def APIExpense(request):
    singleexpense = Expense.objects.all()
    serializer = ExpenseSerializer(singleexpense, many=True)
    # ภาษาไทย json_dumps_params={'ensure_ascii':False}
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST'])
def api_post_expense(request):
   try:
        allexpense = Expense()
        if request.method == 'POST':
            serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
   except:
         return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

def contract(request):
   if request.method=='POST':
      form =contractform(request.POST)
      if form.is_valid():
         form.save()
         return redirect('home-page')
   form =contractform()
   context ={'form':form}
   return render(request,'product/contract.html',context)