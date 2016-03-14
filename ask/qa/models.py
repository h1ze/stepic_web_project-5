from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(User, related_name='question_author_set')
    likes = models.ManyToManyField(User, related_name='question_likes_set')
    
    def get_url(self):
        return reverse('question_details', kwargs={'id': self.id})
        
    def __unicode__(self):
        return self.title
    
    
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User) #, models.SET_NULL, null=True)
