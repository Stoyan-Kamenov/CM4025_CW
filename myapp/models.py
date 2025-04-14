from django.db import models
from django.contrib.auth.models import User
import uuid

class Stories(models.Model):
    storyId = models.UUIDField('Story ID', primary_key=True, default=uuid.uuid4, editable=False) 
    title = models.CharField('Title', max_length=200)
    author = models.CharField('Author', max_length=100)
    content = models.TextField('Story')
    genre = models.CharField('Genre', max_length=50)
    isPublic = models.BooleanField('Is it Public', default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories', null=True, blank=True)

    class Meta:
        verbose_name = 'Stories'
        verbose_name_plural = 'Stories'

    def __str__(self):
        return self.title
    
class Ratings(models.Model):
    storyId = models.ForeignKey(Stories, blank= True, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField('Rating')
    
    class Meta:
        verbose_name = 'Ratings'
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return str(self.rating)