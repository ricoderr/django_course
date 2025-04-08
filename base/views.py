from django.shortcuts import render
from django.http import HttpResponse
from base.models import Product 

def products(request):
    query_set = Product.objects.all()
    query_set.filter().filter().count()
    return HttpResponse("Hellooo")
