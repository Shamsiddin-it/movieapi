from django.urls import path
from .views import *
urlpatterns = [
    path('actor_list/', ActorListAPIView.as_view(), name = 'actor_list'),
    path('actor_create/', ActorCreateAPIView.as_view(), name = 'actor_create'),
    path('actor_update/<int:pk>/', ActorUpdateAPIView.as_view(), name = 'actor_update'),
    path('actor_destroy/<int:pk>/', ActorDestroyAPIView.as_view(), name = 'actor_destroy'),
    path('director_list/', DirectorListAPIView.as_view(), name = 'director_list'),
    path('director_create/', DirectorCreateAPIView.as_view(), name = 'director_create'),
    path('director_update/<int:pk>/', DirectorUpdateAPIView.as_view(), name = 'director_update'),
    path('director_destroy/<int:pk>/', DirectorDestroyAPIView.as_view(), name = 'director_destroy'),
    path('movie_list/', MovieListAPIView.as_view(), name = 'movie_list'),
    path('movie_create/', MovieCreateAPIView.as_view(), name = 'movie_create'),
    path('movie_update/<int:pk>/', MovieUpdateAPIView.as_view(), name = 'movie_update'),
    path('movie_destroy/<int:pk>/', MovieDestroyAPIView.as_view(), name = 'movie_destroy'),
    path('reviewer_list/', ReviewerListAPIView.as_view(), name = 'reviewer_list'),
    path('reviewer_create/', ReviewerCreateAPIView.as_view(), name = 'reviewer_create'),
    path('reviewer_update/<int:pk>/', ReviewerUpdateAPIView.as_view(), name = 'reviewer_update'),
    path('reviewer_destroy/<int:pk>/', ReviewerDestroyAPIView.as_view(), name = 'reviewer_destroy'),
    path('genres_list/', GenresListAPIView.as_view(), name = 'genres_list'),
    path('genres_create/', GenresCreateAPIView.as_view(), name = 'genres_create'),
    path('genres_update/<int:pk>/', GenresUpdateAPIView.as_view(), name = 'genres_update'),
    path('genres_destroy/<int:pk>/', GenresDestroyAPIView.as_view(), name = 'genres_destroy'),
]
