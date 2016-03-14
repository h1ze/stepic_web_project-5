from django.db import models
from django.http import Http404
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def get_questions_by_type(self, question_type):
        if question_type == "" or question_type == "new":
            return self.order_by("-added_at", "-id")
        elif question_type == "popular":
            return self.order_by("-rating", "-id")
        else:
            raise Http404


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="question_author", null=True)
    likes = models.ManyToManyField(User, related_name="question_likes", null=True)

    objects = QuestionManager()

    def __str__(self):
        return self.title

    def get_url(self):
        return "/question/{0}".format(self.id)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, related_name="answer_author", null=True)

    def __str__(self):
        return self.text
