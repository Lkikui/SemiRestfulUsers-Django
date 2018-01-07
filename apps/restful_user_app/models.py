from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name cannot be empty"
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name cannot be empty"
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default = "")
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True) - 8
    objects = UserManager()
    def __str__(self):
        return "<object: {}, {}, {}, {}>".format(self.first_name, self.last_name, self.email, self.created_at)