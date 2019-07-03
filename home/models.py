from django import forms
from django.db import models

class AllData(models.Model):
    finder = models.CharField(max_length=50)
    # decText = models.TextField(blank=True, null=True)
    encText = models.TextField(blank=True, null=True)
    keys = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.finder
