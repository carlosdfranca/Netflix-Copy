from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView


class Homepage(TemplateView):
    template_name = 'homepage.html'

class HomeFilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme
