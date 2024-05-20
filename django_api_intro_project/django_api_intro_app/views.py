from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


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

    def create(self, request):
         #the request is immutable, which is a problem, so we make a copy first
         #a copy of the request data being sent
         mutable_data_copy = request.data.copy()
         mutable_data_copy['name'] = f'Professor {mutable_data_copy['name']}'
         #so we attache the existing item, name and put Professor
         #then we have to serialize it and send it out

         serializer = InstructorSerializer(data=mutable_data_copy)
         #serializer is always looking for either the straight object from the class, or defined data you're passing to it
            #because we're passsing data to it we have to make sure the data is valid
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def destroy(self, request, pk=None):
         # we will pass the pk of the item we will be deleting
         course = self.get_object()
         #this will be the course we're working on
         if Grade.onjects.filter(course=course).exists():
              #then we wanna stop it
              raise ValidationError({'detail': 'Cannot delete course because it has associated grades.'})
         
         self.perform_destroy(course)
         return Response()


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
    
    def update(self, request, pk=None):
         grade = Grade.objects.get(pk=pk)
         grade_serializer = GradeSerializer(data = request.data)
         grade_serializer.is_valid(raise_exception=True)
         grade_serializer.save()

         student = Student.objects.get(id = grade.student.id)
         if (int(request.data['score']) > 90):
              if not student.name.startswith('Brilliant '):
                student.name = f'Brilliant {student.name}'
                student.save()
         else:
            if student.name.startswith('Brilliant '):
                 student.name = student.name.replace('Brilliant ', '')
                 student.save()

         return Response(grade_serializer.data)

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