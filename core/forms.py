from django import forms
from .models import Resposta

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['q1', 'q2', 'q3', 'q4', 'q5a', 'q5b', 'q5c', 'q5d', 'q5e', 'q5f', 'q5g', 'q5h', 'q5i', 'q5j', 'q5j_frequency', 'q6', 'q7', 'q8', 'q9', 'q10']
        
        widgets = {
            'q1': forms.TimeInput(attrs={'type': 'time'}),
            'q2': forms.NumberInput(attrs={'min': 0, 'max': 240}),
            'q3': forms.TimeInput(attrs={'type': 'time'}),
            'q4': forms.TimeInput(attrs={'type': 'time'}),
            'q5a': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q5b': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q5c': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q5d': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q5e': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q5f': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q5g': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q5h': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q5i': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q5j': forms.TextInput(attrs={'class': 'form-control', 'id': 'q5j'}),
            'q5j_frequency': forms.Select(attrs={'style': 'display-none'}, choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q6': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Muito boa'), (1, 'Boa'), (2, 'Ruim'), (3, 'Muito ruim')]),
            'q7': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q8': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma no último mês'), (1, 'Menos de uma vez por semana'), (2, 'Uma ou duas vezes por semana'), (3, 'Três ou mais vezes na semana')]),
            'q9': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Nenhuma dificuldade'), (1, 'Um problema leve'), (2, 'Um problema razoável'), (3, 'Um grande problema')]),
            'q10': forms.Select(choices=[(None, 'Selecione uma opção'), (0, 'Não'), (1, 'Parceiro ou colega, mas em outro quarto'), (2, 'Parceiro no mesmo quarto, mas em outra cama'), (3, 'Parceiro na mesma cama')]),
        }
