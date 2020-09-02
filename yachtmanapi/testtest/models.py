from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)
