from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Content
from .permissions import IsAdminOrReadOnly, IsCourseStudent
from .serializers import ContentSerializer
from courses.models import Course
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotFound

class CreateContentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.filter(course_id=self.kwargs.get("course_id"))
    
    def perform_create(self, serializer):
        found_course = get_object_or_404(Course, pk=self.kwargs.get("course_id"))
        serializer.save(course=found_course)

class RetrieveUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly, IsCourseStudent]
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
  
    # def get_queryset(self):
    #     return Content.objects.filter(course_id=self.kwargs.get("course_id"))
    
    def get_object(self) -> Content:
        content = Content.objects.filter(pk=self.kwargs["content_id"]).first()
        course = Course.objects.filter(pk=self.kwargs["course_id"]).exists()
        if not course:
            raise NotFound({"detail": "course not found."})
        if not content:
            raise NotFound({"detail": "content not found."})
        self.check_object_permissions(self.request, content)
        return content

