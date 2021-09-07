from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    url = models.TextField()
    
    def __str__(self):
       return self.title 
   
class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=100, default="anon")
    title = models.CharField(max_length=225, default="no comments")
    body = models.CharField(max_length=2000, default="no comments")
    
    def __str__(self):
        return self.title