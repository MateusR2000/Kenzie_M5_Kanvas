from django.db import models
import uuid

class StudentCourseStatus(models.TextChoices):
    pending = "pending",
    accepted = "accepted",

class StudentCourse(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    status = models.CharField(
        max_length = 10,
        choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.pending
    )

    student = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="students_courses"
    )

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="students_courses"
    )
