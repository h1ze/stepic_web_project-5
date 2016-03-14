# -*- coding: utf-8 -*-

"""

"""

from django import forms
from django.contrib.auth.models import User

try:
    from stepic_web.ask.qa.models import Question, Answer
except ImportError:
    import sys
    sys.path.append("/home/box")
    from web.ask.qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(min_length=1)
    text = forms.CharField(min_length=1, widget=forms.Textarea)

    def __init__(self, user=None, **kwargs):
        self.user = user
        super(AskForm, self).__init__(kwargs)

    def save(self):
        self.cleaned_data["author"] = self.user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(min_length=1, widget=forms.Textarea)
    question = forms.IntegerField()

    def __init__(self, user=None, **kwargs):
        self.user = user
        super(AnswerForm, self).__init__(kwargs)

    def clean_question(self):
        question_qs = Question.objects.filter(id=self.cleaned_data["question"])
        if len(question_qs) == 1:
            return question_qs[0]
        else:
            raise forms.ValidationError("Strange question")

    def save(self):
        self.cleaned_data["author"] = self.user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField(min_length=1)
    email = forms.EmailField(required=False)
    password = forms.CharField(min_length=1, widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(min_length=1)
    password = forms.CharField(min_length=1, widget=forms.PasswordInput)


if __name__ == '__main__':
    pass
