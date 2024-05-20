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
    letter_grade = serializers.SerializerMethodField()
    # this is us defining our own field, and it will look for a function to populate it, which we make down below
    #we're creating a field that doesn't exist on the model

    class Meta:
        model = Grade
        fields = ['id', 'score', 'course', 'student', 'letter_grade']

    def get_letter_grade(self, obj):
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




# course = Course.objects.get(id=1)

# print('\n****************************************\n')

# print(f'before serializer: {course}')

# course_serializer = CourseSerializer(course)

# print('\n****************************************\n')

# print(f'After serializer: {course_serializer.data}')

# print('\n****************************************\n')
