from django.db import models
from movies.models import Movie, Character
from cast.models import Person
from datetime import datetime

class Reviews(models.Model):
    review = models.CharField(max_length=20000, default='')
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING, related_name="reviews", null=True)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    character = models.ForeignKey(Character, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)