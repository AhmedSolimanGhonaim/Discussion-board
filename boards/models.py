from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Board(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField(max_length=200, blank = True)
    def __str__(self):
        return self.name    
class Topic(models.Model):
    # id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    board = models.ForeignKey(Board, related_name='topics',on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='topics', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    

class Post(models.Model):
    # id = models.AutoField(primary_key=True)
    message = models.TextField()
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    # updated_date = models.DateTimeField(auto_now=True)
