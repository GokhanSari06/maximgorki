from django.shortcuts import render
from .models import BlogIcerik

def blog_listesi(request):
    icerik = BlogIcerik.objects.all()
    return render(request, 'blog/blog_listesi.html', {'icerik':icerik})

def blog_detay(request,link):
	icerik = BlogIcerik.objects.get(link=link)
	return render(request, 'blog/blog_detay.html', {'icerik':icerik})
