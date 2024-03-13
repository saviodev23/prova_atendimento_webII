from rest_framework import serializers
from atendimento.models import Profissional, Atendimento

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendimento
        fields = ['profissional', 'data', 'hora', 'cliente', 'obs']
