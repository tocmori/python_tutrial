from django.db import models

# Create your models here.
class Greeting(models.Model):
    whene = models.DateTimeField('date created', auto_now_add=True)
