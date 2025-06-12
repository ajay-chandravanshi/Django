from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny , IsAdminUser , IsAuthenticatedOrReadOnly
from rest_framework import viewsets

class StudentViewSets(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    permission_classes = [IsAuthenticated] 
    # permission_classes = [AllowAny] 
    # permission_classes = [IsAdminUser] 
   
        