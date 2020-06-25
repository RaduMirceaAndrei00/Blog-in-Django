from django.conf import settings
from django.db import models

class ProjectsAndAchievements(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

class TechnicalSkills(models.Model):
    text = models.TextField()

class Skills(models.Model):
    text = models.TextField()

class Awards(models.Model):
    text = models.TextField()

class Languages(models.Model):
    text = models.TextField()
