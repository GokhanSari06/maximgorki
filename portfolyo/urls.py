from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolyo_listesi),
]
