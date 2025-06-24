from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrOwner
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated & IsAdminOrOwner]
