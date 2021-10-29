from django.db import models

# Create your models here.

class Activity(models.Model):
    activity_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.activity_name

class SubProj(models.Model):
    subproj_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.subproj_name

class Event(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    subproj = models.ForeignKey(SubProj, on_delete=models.CASCADE)
    event_time = models.DateTimeField('event time')