from rest_framework import viewsets, permissions
from .models import Department
from .serializers import DepartmentSerializer

# Create your views here.

class DeparmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
