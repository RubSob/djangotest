from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100, default="silent") 

    def speak(self):
        return f'The {self.name} says "{self.sound}"'

    def __str__(self):
        return self.name