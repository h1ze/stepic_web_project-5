# -*- coding: utf-8 -*-

"""

"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from stepic_web.ask.qa.models import Question, Answer

N_USER = 5
N_QUESTION = N_USER * 5
N_ANSWER = N_QUESTION * 3


def fill_db():
    for user_num in range(N_USER):
        username = "user_{0}".format(user_num)
        email = "user_{0}@email.com".format(user_num)

        User.objects.get_or_create(username=username, email=email)

    for question_num in range(N_QUESTION):
        title = "question_{0}".format(question_num)
        text = "question_text_{0}".format(question_num)
        rating = question_num - N_QUESTION // 2

        username = "user_{0}".format(question_num % N_USER)
        author = User.objects.get(username=username)

        Question.objects.get_or_create(title=title, text=text, rating=rating, author=author)

    for answer_num in range(N_ANSWER):
        text = "answer_text_{0}".format(answer_num)

        question_title =  "question_{0}".format(answer_num % N_QUESTION)
        question = Question.objects.get(title=question_title)

        username = "user_{0}".format(answer_num % N_USER)
        author = User.objects.get(username=username)

        Answer.objects.get_or_create(text=text, question=question, author=author)


class Command(BaseCommand):
    def handle(self, **options):
        fill_db()


if __name__ == '__main__':
    pass