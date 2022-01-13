from django.db import models

# Create your models here.
class Programa(models.Model):
    TIPO = (('S', 'Serie'), ('F', 'Filme'),)
    CATEGORIA = (('T', 'Terror'), ('C', 'Comedia'), ('A', 'Animação'),
     ('AV', 'Aventura'), ('AC', 'Ação'),)

    titulo = models.CharField(max_length=60)
    data_lancamento = models.DateField()
    duracao = models.IntegerField()
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False)
    categoria = models.CharField(max_length=2, choices=CATEGORIA, blank=False, default='', null=False)



