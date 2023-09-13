from django.db import models
from cast.models import Person
from datetime import datetime
import json

class Movie(models.Model):
    title = models.CharField(50, default='')
    description = models.CharField(max_length=20000, default='')
    director = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    actors = models.CharField(max_length=2000, default='')
    
class Character(models.Model):
    character = models.CharField(max_length=50, default='')
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)