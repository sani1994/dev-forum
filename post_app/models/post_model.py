from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    updated_by = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f'{self.title[:20]} ... by {self.created_at.username}'