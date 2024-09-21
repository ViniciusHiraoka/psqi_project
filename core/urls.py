# onde fica localizado as "path", o caminho das rotas
from django.urls import path
from .views import index, questionario, resultado

urlpatterns = [
    path('', index, name='index'),
    path('questionario/', questionario, name='questionario'),
    path('resultado/<int:questionario_id>/', resultado, name='resultado')
]