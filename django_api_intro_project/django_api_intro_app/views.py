from rest_framework import viewsets
from rest_framework.response import Response


from .models import *
#can do .models as opposed to a more explicit path because we're in same folder

from .serializers import *
# we are going to use the serialized data here so we need it all

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    #two things going on that are pretty much always there, queryset based on what we want to look at (which you can filter down but we won't here)
    #this is all the students
    queryset = Student.objects.all()
    #and what serializer to use, it will be the student serializer
    #this is basically the endpoint, but we need to register it in the url
    serializer_class = StudentSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def retrieve(self, request, pk=None):
         grade = Grade.objects.get(pk=pk)
         grade_serializer = GradeSerializer(grade)
         #every serializer has a .data attached
         data = grade_serializer.data
         data['letter_grade'] = get_letter_grade(grade)
         return Response(data)

def get_letter_grade(obj):
            if (obj.score >= 90):
                return 'A'
            elif (obj.score >= 80):
                return 'B'
            elif (obj.score >= 70):
                return 'C'
            elif (obj.score >= 60):
                return 'D'
            else:
                return 'F'