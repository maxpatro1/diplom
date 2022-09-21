from django.db import models
from django.contrib.auth.models import User


class Permission(models.Model):
    name = models.CharField(max_length=250)


class Role(models.Model):
    name = models.CharField(max_length=250)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


class Dict_Group(models.Model):
    name = models.CharField(max_length=250)


# class Executor(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.CharField(max_length=200)
#     group = models.ForeignKey(Dict_Group, on_delete=models.CASCADE)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "{}, email: {}".format(self.user, self.email)


class Course(models.Model):
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=1000)
    deadline = models.DateTimeField(null=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.description)


class Lab(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    deadline = models.DateTimeField(null=True)

    def __str__(self):
        return "{}, {}".format(self.name, self.description)


class User_Has_Labs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    lab_file_name = models.CharField(max_length=1000, null=True)
    is_compile = models.BooleanField(default=False)


class User_Has_Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_compile = models.BooleanField(default=False)
