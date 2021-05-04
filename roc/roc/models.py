from cms.models.pluginmodel import CMSPlugin

from django.db import models

class Blog(CMSPlugin):
    title = models.CharField(max_length=50, default='Title')
    body = models.CharField(max_length=1000, default='blog')
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    sub = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")