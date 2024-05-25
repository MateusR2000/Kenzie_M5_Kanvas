from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminOrReadOnly, IsCourseStudent
from .serializers import CourseSerializer
from .models import Course
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound

class ListCreateCourseView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly, IsCourseStudent]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset.all()
        else:
            return Course.objects.filter(students=self.request.user)


class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"

    def get_object(self):
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        if not course:
            raise NotFound({"detail": "course not found."})
        return course

    
