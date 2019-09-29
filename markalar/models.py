from django.db import models

class MarkalarIcerik(models.Model):
    title = models.CharField(max_length=30)
    resim = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['id']

