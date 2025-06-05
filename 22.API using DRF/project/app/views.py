from .models import Student
from .serializer import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST'])
def student_list(request):
    if request.method=='GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET','PUT','DELETE','PATCH'])

def student_detail(request,pk):
    id=Student.objects.filter(id=pk)
    if id:
        if request.method=='GET':
            Student = Student.objects.get(id=pk)
            serializer = student_detail(Student)
            return Response(serializer.data)
        
        elif request.method=='PUT':
            Student = Student.objects.get(id=pk)
            serializer = StudentSerializer(Student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
        elif request.method=='PATCH':
            Student = Student.objects.get(id=pk)
            serializer = StudentSerializer(Student, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        
        elif request.method=='DELETE':
            Student = Student.objects.get(id=pk)
            Student.delete()
            return Response({'msg':"Data deleted successfully"})
        
        else:
            res={'msg':"Not Present in database!!"}
            return Response(res)
