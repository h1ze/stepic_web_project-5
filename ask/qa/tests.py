import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = "stepic_web.ask.ask.settings"
django.setup()

import math

from django.test import TestCase

from stepic_web.ask.qa.management.commands.fill_db import fill_db
from stepic_web.ask.qa.models import Question, Answer
from stepic_web.ask.qa.views import build_url, LIMIT


class GetQuestionsTest(TestCase):
    def setUp(self):
        fill_db()

    def test_first_page(self):
        urls = {"/": "new", "/new/": "new", "/popular/": "popular"}

        for url, question_type in urls.items():
            questions = Question.objects.get_questions_by_type(question_type)
            n_question = len(questions)

            response = self.client.get(url)
            self.assertContains(response, '"{0}"'.format(questions[0].get_url()))
            if n_question > LIMIT:
                self.assertNotContains(response, '"{0}"'.format(questions[n_question-1].get_url()))

    def test_last_page(self):
        urls = {"/": "new", "/new/": "new", "/popular/": "popular"}

        for url, question_type in urls.items():
            questions = Question.objects.get_questions_by_type(question_type)
            n_question = len(questions)

            last_page_num = math.ceil(n_question / LIMIT)
            params = {"page": last_page_num}
            response = self.client.get(build_url(url, params))
            self.assertContains(response, '"{0}"'.format(questions[n_question-1].get_url()))


class GetCurrentQuestionTest(TestCase):
    def setUp(self):
        fill_db()

    def test_answer(self):
        question = Question.objects.first()
        response = self.client.get("/question/{0}/".format(question.id))
        self.assertContains(response, "Answer by", len(Answer.objects.filter(question=question)))

    def test_answer_404(self):
        response = self.client.get("/question/-1/")
        self.assertEqual(response.status_code, 404)

    def test_right_new_answer(self):
        question = Question.objects.first()
        prev_num_answers = len(Answer.objects.filter(question=question))
        response = self.client.post("/question/{0}/".format(question.id), {"text": "text", "question": question.id})
        self.assertEqual(prev_num_answers+1, len(Answer.objects.filter(question=question)))
        self.assertEqual(response.status_code, 302)

    def test_wrong_new_answer(self):
        question = Question.objects.first()
        response = self.client.post("/question/{0}/".format(question.id), {"text": "", "question": question.id})
        self.assertEqual(response.status_code, 200)


class AskQuestionTest(TestCase):
    def setUp(self):
        fill_db()

    def test_right_new_question(self):
        prev_num_questions = Question.objects.count()
        response = self.client.post("/ask/", {"text": "text", "title": "title"})
        self.assertEqual(prev_num_questions+1, Question.objects.count())
        self.assertEqual(response.status_code, 302)

    def test_wrong_new_question(self):
        response = self.client.post("/ask/", {"text": "", "title": ""})
        self.assertEqual(response.status_code, 200)