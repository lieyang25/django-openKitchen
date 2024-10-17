"""定义当前myKitchen的URL模式"""
from django.urls import path

from . import views

app_name = 'myKitchen'
urlpatterns = [
    #主页
    path('',views.index,name='index'),
    path('pizzas/',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>',views.pizza,name='pizza')
]