from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime

from movies.models import Character
from movies.api.serializers import CharacterSerializer

class CharacterCreateAPIView(APIView):

    def get(self, request):
        character = Character.objects
        serializer = CharacterSerializer(character, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CharacterDetailAPIView(APIView):

    def get_character(self, pk):
        character= get_object_or_404(character, pk=pk)
        return character
    
    def get(self, request, pk):
        character = self.get_character(pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    
    def put(self, request, pk):
        character = self.get_character(pk)
        serializer = CharacterSerializer(character, data=request.data)
        
        
        if serializer.is_valid():
            serializer.validated_data["updated_at"] = datetime.now()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        character = self.get_character(pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)