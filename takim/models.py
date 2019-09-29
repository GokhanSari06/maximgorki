from django.db import models

class TakimIcerik(models.Model):
    title = models.CharField(max_length=100, default='Blog İçerik')
    description = models.CharField(max_length=100, default='Description')
    keywords = models.CharField(max_length=100, default='Keywords')
    author = models.CharField(max_length=100, default='Author')
    isim = models.CharField(max_length=100)
    pozisyon = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    pinterest = models.CharField(max_length=100)
    resim = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.isim
