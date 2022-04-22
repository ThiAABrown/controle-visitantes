from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from visitantes.models import Visitante

from django.utils import timezone

@login_required
def index(request):

    todos_visitantes = Visitante.objects.order_by(
        "-horario_chegada"
    )

    visitantes_aguardando = todos_visitantes.filter(
        status="AGUARDANDO"
    )

    visitantes_em_visita = todos_visitantes.filter(
        status="EM_VISITA"
    )

    visitantes_finalizado = todos_visitantes.filter(
        status="FINALIZADO"
    )

    hora_atual = timezone.now()
    mes_atual = hora_atual.month

    visitantes_mes = todos_visitantes.filter(
        horario_chegada__month=mes_atual
    )

    search = request.GET.get('visitantes-search')
    if search:
        todos_visitantes=todos_visitantes.filter(nome_completo__icontains=search)


    context = {
        "nome_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizado": visitantes_finalizado.count(),
        "visitantes_mes": visitantes_mes.count(),
    }


    return render(request, "index.html", context)

@login_required
def visitantes_aguardando(request):
    todos_visitantes = Visitante.objects.order_by(
        "-horario_chegada"
    )
    visit_aguardando = todos_visitantes.filter(
    status="AGUARDANDO"
    )
    nome_pagina = "Visitantes aguardando autorizção"
    context = {
        "total_visitantes_aguardando": visit_aguardando.count(),
        "visitantes_aguardando": visit_aguardando,
        "nome_pagina": nome_pagina
    }

    return render(request, "visitantes_aguardando.html", context )

@login_required
def visitantes_emvisita(request):
    todos_visitantes = Visitante.objects.order_by(
        "-horario_chegada"
    )
    visit_emvisita = todos_visitantes.filter(
    status="EM_VISITA"
    )
    nome_pagina = "Visitantes em visita"
    context = {
        "total_visitantes_em_visita": visit_emvisita.count(),
        "visitantes_emvisita": visit_emvisita,
        "nome_pagina": nome_pagina
    }

    return render(request, "visitantes_emvisita.html", context )