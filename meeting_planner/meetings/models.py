from datetime import time
from django.contrib.auth.models import User
from django.db import models
from django import forms


class Comment(models.Model):
    meeting = models.ForeignKey('meetings.Meeting', on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

class Participants(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    participants = models.CharField(max_length=255)
    notes = models.TextField(default='none')

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

    def get_participants_list(self):
        return self.participants.split(',')