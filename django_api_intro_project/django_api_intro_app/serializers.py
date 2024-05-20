from rest_framework import serializers
from .models import *
#could do one by one like: from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #what model did we attach it to? Student
        #what fields do we want to translate:
        fields = ['id', 'name', 'age', 'courses']

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'instructor']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'score', 'course', 'student']