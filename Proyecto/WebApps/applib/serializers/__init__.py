from .AuthorSerializer import AuthorSerializer
from .AuthorDetailSerializer import AuthorDetailSerializer
from .BookSerializer import BookSerializer
from .BookDetailSerializer import BookDetailSerializer
from .BookCopySerializer import BookCopySerializer
from .BookCopyDetailSerializer import BookCopyDetailSerializer
from .CategorySerializer import CategorySerializer
from .CategoryDetailSerializer import CategoryDetailSerializer
from .LoanSerializer import LoanSerializer
from .LoanDetailSerializer import LoanDetailSerializer
from .UserSerializer import UserSerializer
from .UserDetailSerializer import UserDetailSerializer

# Definimos la lista pública de lo que el módulo exporta al exterior
__all__ = [
    'AuthorSerializer',
    'AuthorDetailSerializer',
    'BookSerializer',
    'BookDetailSerializer',
    'BookCopySerializer',
    'BookCopyDetailSerializer',
    'CategorySerializer',
    'CategoryDetailSerializer',
    'LoanSerializer',
    'LoanDetailSerializer',
    'UserSerializer',
    'UserDetailSerializer',
]