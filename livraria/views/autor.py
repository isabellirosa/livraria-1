from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from livraria.models import  Autor
from livraria.serializers import AutorSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["nome", "email"]
    search_fields = ["nome", "email"]