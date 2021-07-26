from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return self.role_name


class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    patronymic_name = models.CharField(max_length=40)
    password = models.CharField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
