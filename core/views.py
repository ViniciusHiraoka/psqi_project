from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionario, Resposta
from .forms import RespostaForm
from django.contrib.auth.decorators import login_required
from datetime import time

def time_to_float(t):
    """Converte um objeto datetime.time em horas como um valor de ponto flutuante."""
    return t.hour + t.minute / 60.0

def calculate_component(mapping, value):
    """Retorna a pontuação correspondente ao valor de acordo com o mapeamento."""
    for threshold, score in mapping.items():
        if value <= threshold:
            return score
    return max(mapping.values())  # Retorna a maior pontuação se não houver correspondência

def calculate_sleep_efficiency(sleep_hours, bedtime, wakeup_time):
    """Calcula a eficiência do sono com base nas horas de sono e tempo na cama."""
    bedtime_hours = time_to_float(bedtime)
    wakeup_hours = time_to_float(wakeup_time)
    
    # Calcula o tempo total na cama (em horas)
    hours_in_bed = wakeup_hours - bedtime_hours
    if hours_in_bed < 0:
        hours_in_bed += 24  # Ajusta para o caso de dormir em um dia e acordar no outro

    # Calcula a eficiência do sono
    return (sleep_hours / hours_in_bed) * 100 if hours_in_bed > 0 else 0

def calculate_psqi_score(assessment):
    # Mapeamentos
    mappings = {
        'latency': {15: 0, 30: 1, 60: 2, float("inf"): 3},
        'duration': {7: 0, 6: 1, 5: 2, float("inf"): 3},
        'efficiency': {85: 0, 84: 1, 74: 2, float("inf"): 3},
        'disturbances': {0: 0, 9: 1, 18: 2, float("inf"): 3},
        'dysfunction': {0: 0, 2: 1, 4: 2, float("inf"): 3}
    }

    # Componentes individuais
    component_1 = assessment.q6 if assessment.q6 is not None else 0  # Qualidade do sono
    component_2 = calculate_component(
        mappings['latency'], 
        (assessment.q2 if assessment.q2 is not None else 0) + (assessment.q5a if assessment.q5a is not None else 0)
    )  # Latência do sono

    # Convertendo campos TimeField para valores flutuantes
    component_3 = calculate_component(mappings['duration'], time_to_float(assessment.q4) if assessment.q4 else 0)  # Duração do sono
    
    # Eficiência do sono
    sleep_efficiency = calculate_sleep_efficiency(
        time_to_float(assessment.q4) if assessment.q4 else 0,  # Horas de sono
        assessment.q3 if assessment.q3 else time(0, 0),  # Hora de acordar
        assessment.q1 if assessment.q1 else time(0, 0)   # Hora de dormir
    )
    component_4 = calculate_component(mappings['efficiency'], sleep_efficiency)

    # Distúrbios (soma dos distúrbios)
    disturbances_sum = sum([
        assessment.q5b if assessment.q5b is not None else 0,
        assessment.q5c if assessment.q5c is not None else 0,
        assessment.q5d if assessment.q5d is not None else 0,
        assessment.q5e if assessment.q5e is not None else 0,
        assessment.q5f if assessment.q5f is not None else 0,
        assessment.q5g if assessment.q5g is not None else 0,
        assessment.q5h if assessment.q5h is not None else 0,
        assessment.q5i if assessment.q5i is not None else 0,
        assessment.q5j_frequency if assessment.q5j_frequency is not None else 0
    ])
    component_5 = calculate_component(mappings['disturbances'], disturbances_sum)

    # Outros componentes
    component_6 = assessment.q7 if assessment.q7 is not None else 0  # Uso de medicação
    component_7 = calculate_component(
        mappings['dysfunction'], 
        (assessment.q8 if assessment.q8 is not None else 0) + (assessment.q9 if assessment.q9 is not None else 0)
    )  # Disfunção diurna

    # Soma total dos componentes
    total_score = sum([component_1, component_2, component_3, component_4, component_5, component_6, component_7])

    if total_score > 5:
        sleep_quality = 'sono insatisfatório (baixa qualidade do sono).'
    else:
        sleep_quality = 'sono satisfatório (boa qualidade do sono).'

    return total_score, sleep_quality

def index(request):
    return render(request, 'index.html')


@login_required
def questionario(request):
    if request.method == 'POST':
        form = RespostaForm(request.POST)
        
        if form.is_valid():
            # Criar um novo questionário para cada envio
            questionario = Questionario.objects.create(usuario=request.user)

            # Salvar a nova resposta relacionada ao novo questionário
            nova_resposta = form.save(commit=False)
            nova_resposta.usuario = request.user
            nova_resposta.questionario = questionario
            nova_resposta.save()

            # Redirecionar para o resultado do novo questionário
            return redirect('resultado', questionario_id=questionario.id)
    else:
        # Sempre mostrar o formulário em branco
        form = RespostaForm()
    
    return render(request, 'questionario.html', {'form': form}) 

@login_required
def resultado(request, questionario_id):
    questionario = get_object_or_404(Questionario, id=questionario_id, usuario=request.user)
    respostas = Resposta.objects.get(questionario=questionario)
    total_score, sleep_quality = calculate_psqi_score(respostas)

    context = {
        'questionario': questionario,
        'respostas': respostas,
        'total_score': total_score,
        'sleep_quality': sleep_quality
    }

    return render(request, 'resultado.html', context)