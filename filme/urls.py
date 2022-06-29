from django.urls import path
from .views import HomeFilmes, Homepage

urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes', HomeFilmes.as_view()),
]