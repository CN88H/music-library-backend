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
