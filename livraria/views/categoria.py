
from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated

from livraria.models import Categoria
from livraria.serializers import CategoriaSerializer
# from django_filters.rest_framework import DjangoFilterBackend, SearchFilter, OrderingFilter

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # permission_classes = [IsAuthenticated]
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["descricao"]
    search_fields = ["descricao"]
    ordering_fields = ["descricao"]
    ordering = ["descricao"]