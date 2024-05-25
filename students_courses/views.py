from rest_framework.generics import RetrieveUpdateAPIView
from .models import StudentCourse
from courses.models import Course
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAdminOrReadOnly
from .serializers import StudentCoursesSerializer, PartialCourseSerializer
from django.shortcuts import get_object_or_404

class RetrieveUpdateStudentCourseView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PartialCourseSerializer

    queryset = Course.objects.all()
    lookup_url_kwarg = "course_id"
    


    