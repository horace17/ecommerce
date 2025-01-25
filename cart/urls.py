
from django.urls import path
from .  import views

urlpatterns = [
    path('', views.cart_ , name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('payment', views.payment, name='payment'),
    path('add/', views.add_item, name='add_item'),
    path('delete/', views.delete_item, name='delete_item'),
    path('update/', views.update_item, name='update_item'),
]
