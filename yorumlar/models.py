from django.db import models

class YorumlarIcerik(models.Model):
    isim = models.CharField(max_length=30)
    yorum = models.CharField(max_length=300)

    def __str__(self):
        return self.isim

