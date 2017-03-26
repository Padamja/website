from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Tutor(models.Model):
    appuser = models.ForeignKey(User)


class Student(models.Model):
    pass


class TutionCentre(models.Model):
    pass
