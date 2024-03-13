from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from atendimento.views import AtendimentoViewSet
from profissional.views import ProfissionalViewSet

#swagger
from api_atendimentos_webII.swagger import urlpatterns as swagger_urls

router = routers.DefaultRouter()
router.register('api/profissionais', ProfissionalViewSet)
router.register('api/atendimentos', AtendimentoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + swagger_urls

