from django.urls import path
from .views import LivroListCreateView, LivroDetailView

urlpatterns = [
    path('livro/', LivroListCreateView.as_view(), name='livro-list-create'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro-detail'),
]