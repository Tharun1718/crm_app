from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>',views.view_customer,name='view_customer'),
    path('add/',views.add,name='add'),
]