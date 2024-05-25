from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Account(AbstractUser):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    is_superuser = models.BooleanField(default=False)

    my_courses = models.ManyToManyField(
        "courses.Course",
        related_name="my_courses",
        through="students_courses.StudentCourse"
    )