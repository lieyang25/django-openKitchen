from lib2to3.fixes.fix_input import context
from pydoc_data.topics import topics

from django.shortcuts import render

from .models import Pizza
# Create your views here.
def index(request):
    """披萨店主页"""
    return render(request,'myKitchen/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('time_added')
    context = {'pizzas':pizzas}
    return render(request,'myKitchen/pizzas.html',context)

def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    entries = pizza.entry_set.order_by('-date_added')
    context = {'pizza':pizza,'entries':entries}
    return render(request,'myKitchen/pizza.html',context)