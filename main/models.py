from django.db import models

class Biography(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    launch_date = models.DateField()

    def __str__(self):
        return self.name

class Training(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
