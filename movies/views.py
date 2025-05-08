from django.db.models import Count,Avg
from rest_framework import generics, views, response, status
from movies.models import Movies
from reviews.models import Review
from movies.serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()

    def get(self, request):

        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={
                "total movies":total_movies,
                "movies by genre":movies_by_genre,
                "total de reviews":total_reviews,
                "average stars": round(average_stars,2) if average_stars else 0
                },
            status=status.HTTP_200_OK
        )