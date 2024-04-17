from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from usuario.router import router as usuario_router
from uploader.router import router as uploader_router

from livraria.views import CategoriaViewSet, EditoraViewSet, AutorViewSet, LivroViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"autor", AutorViewSet)
router.register(r"livro", LivroViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
