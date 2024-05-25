from django.db import models
import uuid

class Content(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=150)
    content = models.TextField()
    video_url = models.CharField(max_length=200)

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="contents"
    )