from django.db import models

# Create your models here.

class Note(models.Model):
    note =  models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    
    
    