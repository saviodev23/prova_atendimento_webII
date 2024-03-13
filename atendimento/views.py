from rest_framework import viewsets, filters
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication

from .models import Atendimento
from api_atendimentos_webII.serializers import AtendimentoSerializer

class AtendimentoViewSet(viewsets.ModelViewSet):
    """Listando Atendimentos"""
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['profissional']#ordenando atendimento por profissional
    search_fields = ['id', ]#possibilita fazer a busca por id
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
