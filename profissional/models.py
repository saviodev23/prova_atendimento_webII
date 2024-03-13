from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    especialidade = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome