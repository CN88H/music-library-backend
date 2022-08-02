from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MusicLibrarySerializer
from .models import MusicLibary

@api_view(['GET', 'POST'])
def music_list(request):

    if request.method == 'GET':
        musics = MusicLibary.objects.all()
        serializer = MusicLibrarySerializer(musics, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicLibrarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'Put', 'DELETE'])
def music_detail(request, pk):
        music = get_object_or_404(MusicLibary, pk=pk)
        if request.method == 'GET':
            serializer = MusicLibrarySerializer(music)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = MusicLibrarySerializer(music, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == 'DELETE':
            music.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

