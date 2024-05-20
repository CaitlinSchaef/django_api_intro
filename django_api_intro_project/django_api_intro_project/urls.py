"""
URL configuration for django_api_intro_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework import routers
from django.urls import path, include

from django_api_intro_app.views import InstructorViewSet, StudentViewSet, CourseViewSet, GradeViewSet
#giving it the app folder and the views from that

#now define router:
router = routers.DefaultRouter()
#default from rest framework


# from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]



#now register endpoints/viewsets

router.register(r'students', StudentViewSet)
router.register(r'instructors', InstructorViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'grades', GradeViewSet)
#you connect the viewpoint to the student, so if they hit students in their URL it connects it

#making a path and then we're making it include all of the paths in the router
urlpatterns = [
 path('', include(router.urls))
]

"""
    Get
    http://the-name-of-my-website/students
    /students is what we just made to register
    If we hit that url with a request, you'll get a list of all students
    OR
    We can give it more information
    We can pass an id and get a specific student

    Get
    /students/{id}
    a specific student

    POST
    /students/
    (same route but when you send it, the person is saying post instead of get so we know we should be creating not posted)
    this will create a new student

    PUT
    /students/{id}
    this will update a specific student

    DELETE
    /student/{id}
    deletes a specific student

"""