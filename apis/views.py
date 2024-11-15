from .serializers import *
from rest_framework import generics

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorCreateAPIView(generics.CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDestroyAPIView(generics.DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorCreateAPIView(generics.CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDestroyAPIView(generics.DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDestroyAPIView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewerListAPIView(generics.ListAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ReviewerCreateAPIView(generics.CreateAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ReviewerUpdateAPIView(generics.RetrieveAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ReviewerDestroyAPIView(generics.DestroyAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer


class GenresListAPIView(generics.ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer

class GenresCreateAPIView(generics.CreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer

class GenresUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer

class GenresDestroyAPIView(generics.DestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


