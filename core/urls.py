from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homepage'),
    path('apartment_detail/<int:pk>/',views.detail, name='detail'),
]
