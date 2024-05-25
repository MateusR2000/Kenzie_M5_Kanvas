from django.urls import path
from . import views

urlpatterns = [
    path("courses/<uuid:course_id>/students/", views.RetrieveUpdateStudentCourseView.as_view())
]