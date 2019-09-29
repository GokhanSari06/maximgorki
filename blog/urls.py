from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_listesi),
    path("<slug:link>/", views.blog_detay, name ="detail"),
]
