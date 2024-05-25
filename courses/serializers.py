from rest_framework import serializers
from .models import Course
from rest_framework.validators import UniqueValidator
from students_courses.serializers import StudentCoursesSerializer
from contents.serializers import ContentSerializer

class CourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCoursesSerializer(many=True, read_only=True)
    contents = ContentSerializer(many=True, read_only=True)

    
    class Meta:
        model = Course
        fields = ["id", "name", "status", "start_date", "instructor", "end_date", "students_courses", "contents"]
        
        extra_kwargs = {"name": {
                            "validators": [
                                UniqueValidator(
                            queryset=Course.objects.all(),
                            message="course with this name already exists.",
                        )
                    ]
                },
                "instructor": {"required": False}}

