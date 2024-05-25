from rest_framework import serializers
from .models import StudentCourse
from courses.models import Course
from accounts.models import Account

class StudentCoursesSerializer(serializers.ModelSerializer):
    student_username = serializers.CharField(read_only=True, source="student.username")
    student_email = serializers.CharField(source="student.email")

    class Meta:
        model = StudentCourse
        fields = ["id", "status", "student_id", "student_username", "student_email"]

        extra_kwargs = {"id": {"read_only": True}}

class PartialCourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCoursesSerializer(many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]

        extra_kwargs = {"name": {"read_only": True}}

    def update(self, instance, validated_data):
        students = []
        emails = []

        for key in validated_data["students_courses"]:
            print(validated_data)
            student_course = key["student"]
            find_student =  Account.objects.filter(email=student_course["email"]).first()
            if find_student:
                students.append(find_student)
            else:
                emails.append(student_course["email"])
        
        if emails:
            raise serializers.ValidationError({"detail": f"No active accounts was found: {', '.join(emails)}."})
        
        if not self.partial:
            instance.students.add(*students)
            return instance
        
        return super().update(instance, validated_data)


        
