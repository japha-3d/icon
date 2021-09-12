from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required


app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
   
   
]
