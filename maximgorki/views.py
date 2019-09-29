from django.http import HttpResponse
from django.shortcuts import render
from blog.models import BlogIcerik
from hakkimizda.models import HakkimizdaIcerik
from hizmetlerimiz.models import HizmetlerimizIcerik
from markalar.models import MarkalarIcerik
from portfolyo.models import PortfolyoIcerik
from takim.models import TakimIcerik
from yorumlar.models import YorumlarIcerik

def index(request):
    blogicerik = BlogIcerik.objects.all()[:3]
    hakkimizdaicerik = HakkimizdaIcerik.objects.all().order_by("-pk")
    hizmetlerimizicerik = HizmetlerimizIcerik.objects.all().order_by("-pk")
    markalaricerik = MarkalarIcerik.objects.all().order_by("-pk")
    portfolyoicerik = PortfolyoIcerik.objects.all().order_by("-pk")
    takimicerik = TakimIcerik.objects.all().order_by("-pk")
    yorumlaricerik = YorumlarIcerik.objects.all().order_by("-pk")
    return render(request, 'index.html', {'blogicerik':blogicerik, 'hakkimizdaicerik':hakkimizdaicerik,
                                          'hizmetlerimizicerik':hizmetlerimizicerik,
                                          'markalaricerik':markalaricerik, 'portfolyoicerik':portfolyoicerik,
                                          'takimicerik':takimicerik, 'yorumlaricerik':yorumlaricerik})
