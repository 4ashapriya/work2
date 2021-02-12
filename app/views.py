from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def student_api(request):

    if(request.method == 'GET'):
        stu = Student.objects.all()
        serializer= StudentSerializer(stu, many= True)
        return Response(serializer.data)

    if (request.method == 'POST'):
        data = request.data
        serializer = StudentSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':"Data has been created successfully"}
            return Response(res, status= HTTP_201_CREATED)
        return Response({'msg':serializer.errors})



