from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre


class GenreView(ViewSet):
    """Tuna api genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single genre

        Returns:
            Response -- JSON serialized genre
        """
        try:
            genre = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(genre)
            return Response(serializer.data)
        except Genre.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all genres

        Returns:
            Response -- JSON serialized list of genres
        """
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
        
      
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized genre instance
        """
        genre = Genre.objects.create(
            description=request.data["description"],
        )
        serializer = GenreSerializer(genre)
        return Response(serializer.data)  
    
class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genres
    """
    class Meta:
        model = Genre
        fields = ('id', 'description')
