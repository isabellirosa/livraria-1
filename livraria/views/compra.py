from rest_framework.viewsets import ModelViewSet

from livraria.models import Compra
from livraria.serializers import CompraSerializer, CriarEditarCompraSerializer
from django_filters.rest_framework import DjangoFilterBackend



class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["usuario", "status", "data"]
    search_fields = ["usuario__email","status"]

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Compra.objects.all()
        if usuario.groups.filter(name="Administradores"):
            return Compra.objects.all()
        return Compra.objects.filter(usuario=usuario)      
    
    def get_serializer_class(self):
        if self.action == "create" or self.action =="update":
            return CriarEditarCompraSerializer
        return CompraSerializer