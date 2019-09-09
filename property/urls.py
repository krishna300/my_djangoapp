from django.urls import path
from . import views

app_name ='property'

urlpatterns = [
    path('', views.index),
    path('list/', views.property_list),
    path('<int:id>/', views.property_detail,name ='property_detail1'),

]