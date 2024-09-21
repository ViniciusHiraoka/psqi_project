from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# models.py
class Questionario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Questionário {self.id} - {self.usuario.username}'

class Resposta(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    q1 = models.TimeField(null=True, blank=False)
    q2 = models.IntegerField(null=True, blank=False)
    q3 = models.TimeField(null=True, blank=False)
    q4 = models.TimeField(null=True, blank=False)
    q5a = models.IntegerField(null=True, blank=False)
    q5b = models.IntegerField(null=True, blank=False)
    q5c = models.IntegerField(null=True, blank=False)
    q5d = models.IntegerField(null=True, blank=False)
    q5e = models.IntegerField(null=True, blank=False)
    q5f = models.IntegerField(null=True, blank=False)
    q5g = models.IntegerField(null=True, blank=False)
    q5h = models.IntegerField(null=True, blank=False)
    q5i = models.IntegerField(null=True, blank=False)
    q5j = models.TextField(null=True, blank=True, max_length=255)
    q5j_frequency = models.IntegerField(null=True, blank=True)
    q6 = models.IntegerField(null=True, blank=False)
    q7 = models.IntegerField(null=True, blank=False)
    q8 = models.IntegerField(null=True, blank=False)
    q9 = models.IntegerField(null=True, blank=False)
    q10 = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return f'Resposta {self.id} do Questionário {self.questionario.id} por {self.usuario.username}'
