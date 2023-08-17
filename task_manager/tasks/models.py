from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.PROTECT)
    date_of_create = models.DateTimeField(auto_now_add=True)
    label = models.CharField()
