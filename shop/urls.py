from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('bikes/', views.IndexView.as_view(), name='bikes'),
    path('bikes/<int:pk>/', views.BikeView.as_view(), name='bike_detail'),
    path('order/<int:order_no>/', views.OrderView.as_view(), name='order_detail'),
]
