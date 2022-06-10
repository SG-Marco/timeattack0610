from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('products/', views.show_product, name='show_product'),
    path('order/', views.order, name='order'),

]


    