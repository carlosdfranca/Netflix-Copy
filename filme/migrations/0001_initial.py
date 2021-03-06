# Generated by Django 4.0.5 on 2022-06-14 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('thumb', models.ImageField(upload_to='thumb_filmes')),
                ('description', models.TextField(max_length=500)),
                ('category', models.CharField(choices=[('ANALISES', 'Análises'), ('PROGRAMACAO', 'Apresentação'), ('APRESENTACAO', 'Apresentacao'), ('OUTROS', 'Outros')], max_length=15)),
                ('visualizations', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
