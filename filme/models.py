from django.utils import timezone
from django.db import models


LISTA_CATEGORIAS = (
    ('ANALISES', 'Análises'),
    ('PROGRAMACAO', 'Programação'),
    ('APRESENTACAO', 'Apresentação'),
    ('OUTROS', 'Outros'),
)


# Create your models here.
# Criar o filme
class Filme(models.Model):
    title = models.CharField(max_length=50)
    thumb = models.ImageField(upload_to='thumb_filmes')
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizations = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# Criar os episódeos
