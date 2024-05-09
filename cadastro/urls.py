from django.urls import path
from .import views

from rest_framework_simplejwt.views import (
   TokenRefreshView,
)

urlpatterns = [
    path('token/', views.LivroListCreateView.as_view(), name='livro_list_create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
]