from django.shortcuts import render
from .models import HakkimizdaIcerik

def hakkimizda_listesi(request):
    icerik = HakkimizdaIcerik.objects.all()
    return render(request, 'hakkimizda/hakkimizda_listesi.html', {'icerik':icerik})

