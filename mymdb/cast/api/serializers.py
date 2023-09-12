from rest_framework import serializers
from cast.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id","first_name", "last_name", "biography")
        