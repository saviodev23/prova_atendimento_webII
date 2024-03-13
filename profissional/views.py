from rest_framework import viewsets, filters
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication

from .models import Profissional
from api_atendimentos_webII.serializers import ProfissionalSerializer

class ProfissionalViewSet(viewsets.ModelViewSet):
    """Listando Profissionais"""
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']#ordenando os profissionais por nome
    search_fields = ['id', 'nome']#possibilita fazer a busca por nome e id
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]