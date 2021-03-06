# -*- coding: utf-8 -*-
from django import forms
from qa.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class AskForm(forms.Form): #форма добавления вопроса
    title = forms.CharField(max_length=255, min_length=1) #поле заголовка
    text  = forms.CharField(widget=forms.Textarea, min_length=1) #поле текста вопроса
    
    def save(self):
        question = Question.objects.create(title=self.cleaned_data['title'], text=self.cleaned_data['text'], author=self.author)
        question.save()
        return question
        #return Question.objects.create(**self.cleaned_data)
        
        
    def clean_title(self):
	title = self.cleaned_data['title']
	return title

    
    def clean(self):
        return self.cleaned_data

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text.strip():
            raise forms.ValidationError(u'Текст вопроса пустой!', code=12)
        return text
        
        

class AnswerForm(forms.Form): #форма добавления ответа
    text  = forms.CharField(widget=forms.Textarea, min_length=1)
    question = forms.IntegerField(widget=forms.HiddenInput) #поле для связи с вопросом
    author = 1
    
    def __init__(self, *args, **kwargs):
        self._question = kwargs.pop('_question', None)
        forms.Form.__init__(self, *args, **kwargs)
        

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text.strip():
            raise forms.ValidationError(u'Текст ответа пустой!', code=12)
        return text

#    def clean_question(self):
#        question = self.cleaned_data['question']
#        return question
    
    def save(self):
        self.cleaned_data['question'] = self._question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
    
    def clean(self):
        return self.cleaned_data



class SignupForm(forms.Form) :
	username = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	_pass = ""
 +	
 +	def set_password(self, password) :
 +		self._pass = password
 +		return password
	
	def clean_username(self) :
		username = self.cleaned_data['username']
		return username
		
	def clean_email(self) :
		email = self.cleaned_data['email']
		return email
		
	def clean_password(self) :
		password = self.cleaned_data['password']
		
	def save(self) :
		user = User.objects.create_user(self.clean_username(), self.clean_email(), self._pass)
		return user
	
	def loginUser(self) :
		user = authenticate(username=self.clean_username(), password=self._pass)
		login(request, user)
		return user



class LoginForm(forms.Form) :
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)
	_pass = ""
	
	def set_password(self, password) :
		self._pass = password
		return password
	
	def clean_username(self) :
		username = self.cleaned_data['username']
		return username
		
	def clean_password(self) :
		password = self.cleaned_data['password']
		
	def loginUser(self) :
		user = authenticate(username=self.clean_username(), password=self._pass)
		return user


