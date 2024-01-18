from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    body = models.TextField(max_length=2500)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"