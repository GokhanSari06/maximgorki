from django.urls import path
from . import views

urlpatterns = [
    path('', views.hizmetlerimiz_listesi),
    path("<slug:link>/", views.hizmetlerimiz_detay, name ="detail"),
]
