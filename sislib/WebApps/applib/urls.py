from rest_framework.routers import DefaultRouter
from .views import (
    AuthorViewSet,
    BookCopyViewSet,
    BookViewSet,
    CategoryViewSet,
    LoanViewSet,
    UserViewSet,
)

# Creamos el enrutador automático
router = DefaultRouter()

# Registramos cada una de las vistas con su respectivo prefijo de URL
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'book-copies', BookCopyViewSet, basename='bookcopy')
router.register(r'books', BookViewSet, basename='book')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'loans', LoanViewSet, basename='loan')
router.register(r'users', UserViewSet, basename='user')

# Exportamos las URLs generadas por el router
urlpatterns = router.urls