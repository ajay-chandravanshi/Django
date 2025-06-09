from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentViewSets(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer       