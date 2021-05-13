from django.db import models

from teachers.models import Teacher


class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False)
    start = models.DateField(null=True)
    end = models.DateField(null=True)

    def __str__(self):
        return self.name
