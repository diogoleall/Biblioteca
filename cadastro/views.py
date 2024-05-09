from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Livro
from .serializers import LivroSerializer

class LivroListCreateView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_class = [IsAuthenticated]
    
class LivroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_class = [IsAuthenticated]
    
@api_view(['GET'])
def getRoutes(request):
    routes = ["/cadastro/token", "/cadastro/register", "/cadastro/token/refresh"]
    return Response (routes)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == "GET":
        data = f"Parabéns seu cadastro foi feito com sucesso!"
        return Response ({"response":data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f"Parabéns seu cadastro respondeu ao seu POST request com o texto:{text}"
        return Response ({'response':data}, status=status.HTTP_200_OK)
    return Response ({}, status.HTTP_400_BAD_REQUEST)
    