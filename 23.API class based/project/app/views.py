from .models import Student
from .serializers import StudentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class student_detail(APIView):

        return Response(status=status.HTTP_204_NO_CONTENT)
    

   
