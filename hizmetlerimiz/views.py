from django.shortcuts import render
from .models import HizmetlerimizIcerik

def hizmetlerimiz_listesi(request):
    icerik = HizmetlerimizIcerik.objects.all()
    return render(request, 'hizmetlerimiz/hizmetlerimiz_listesi.html', {'icerik':icerik})

def hizmetlerimiz_detay(request,link):
	icerik = HizmetlerimizIcerik.objects.get(link=link)
	return render(request, 'hizmetlerimiz/hizmetlerimiz_detay.html', {'icerik':icerik})