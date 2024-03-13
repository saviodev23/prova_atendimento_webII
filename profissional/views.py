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
    search_fields = ['id']#possibilita fazer a busca por id
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]