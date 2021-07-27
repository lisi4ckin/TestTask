from django.db import models


class Roles(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name


class Users(models.Model):
    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
