


from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('editproduct/',views.get_products),
]