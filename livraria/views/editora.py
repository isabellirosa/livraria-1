from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from livraria.models import Categoria, Editora, Autor, Livro
from livraria.serializers import EditoraSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["nome", "site"]
    search_fields = ["nome", "site"]