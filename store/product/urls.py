from django.urls import path
from .views import Home,About,APIAllproduct,APIProduct,api_post_allproduct,APIExpense,api_post_expense,contract

urlpatterns = [
    path('', Home,name='home-page'),
    path('about/',About,name='about-page'),
    path('apiproduct/',APIAllproduct,name='api-product'),
    path('apisingle/<int:pk>',APIProduct),
    path('api/create',api_post_allproduct),
    path('apiexpense',APIExpense),
    path('api/expense/create',api_post_expense),
    path('contract/',contract,name='contract-page')
]