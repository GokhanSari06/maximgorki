from django.shortcuts import render
from .models import PortfolyoIcerik

def portfolyo_listesi(request):
    icerik = PortfolyoIcerik.objects.all()
    return render(request, 'portfolyo/portfolyo_listesi.html', {'icerik':icerik})

