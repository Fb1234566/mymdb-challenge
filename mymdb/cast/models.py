from django.db import models
from datetime import datetime

class Person(models.Model):
    firstName = models.CharField(max_length=20, default='')
    lastName = models.CharField(max_length=20, default='') 
    biography = models.CharField(max_length=20000, default='')      
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
