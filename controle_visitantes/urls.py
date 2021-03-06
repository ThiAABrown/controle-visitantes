from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from dashboard.views import index

from visitantes.views import (
    registrar_visitante, informacoes_visitante, finalizar_visita
)
from dashboard.views import visitantes_aguardando, visitantes_emvisita, visitantes_finalizados, visitantes_registrados_mesatual

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="logout.html"
        ),
        name="logout"
    ),

    path(
        "",
        index,
        name="index",
    ),

    path(
        "registrar-visitante/",
        registrar_visitante,
        name="registrar_visitante"
    ),

    path(
        "visitantes/<int:id>/",
        informacoes_visitante,
        name="informacoes_visitante"
    ),

    path(
        "visitantes/<int:id>/finalizar-visita",
        finalizar_visita,
        name="finalizar_visita"
    ),

    path(
        "visitantes-aguardando/",
        visitantes_aguardando,
        name="visitantes_aguardando"
    ),

    path(
        "visitantes-em-visita/",
        visitantes_emvisita,
        name="visitantes_emvisita",
    ),

    path(
        "visitas-finalizadas/",
        visitantes_finalizados,
        name="visitantes_finalizados",
    ),

    path(
        "visitantes-registrados-mes-atual/",
        visitantes_registrados_mesatual,
        name="visitantes_registrados_mesatual",
    ),
]

