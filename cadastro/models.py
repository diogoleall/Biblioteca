from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
    editora = models.CharField(max_length=10)
    ano_publicacao = models.IntegerField()
    
    def __str__(self):
        return self.titulo
    
    
    
    
    
    