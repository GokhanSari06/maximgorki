from django.db import models

class PortfolyoIcerik(models.Model):
    isim = models.TextField(max_length=60, default='İsim')
    islem = models.CharField(max_length=30)
    resim = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.isim

    class Meta:
        ordering = [ 'id']