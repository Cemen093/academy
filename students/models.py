from django.db import models

from courses.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    phone = models.IntegerField(null=False)
    facebook = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
