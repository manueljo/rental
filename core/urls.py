from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='homepage'),
    path('apartment_detail/<int:pk>/',views.detail, name='detail'),
    path('get_map/',views.get_map, name='get_map'),
]
