from django.db import models

class HakkimizdaIcerik(models.Model):
    title = models.CharField(max_length=100, default='Blog İçerik')
    description = models.CharField(max_length=100, default='Description')
    keywords = models.CharField(max_length=100, default='Keywords')
    author = models.CharField(max_length=100, default='Author')
    ustbaslik = models.CharField(max_length=100)
    altbaslik = models.CharField(max_length=100)
    buyukyazi = models.TextField()
    kucukyazi = models.TextField()
    resim = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.yazi[:450] + '...'

