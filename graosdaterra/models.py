from django.db import models

# Create your models here.
class contato(models.Model):
    id_contato = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    telefone = models.IntegerField()
