from django.db import models

# Create your models here.
class Word(models.Model):
    qom = models.CharField(max_length=100, null=True, blank=True)
    dfs = models.TextField(null=True, blank=True)
    syn = models.CharField(max_length=300, null=True, blank=True)
    var = models.CharField(max_length=300, null=True, blank=True)
    see = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.qom or ""
