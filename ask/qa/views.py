from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from qa.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from qa.forms import *


def paginate(request, qs):

    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
        
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1 #raise Http404
        
    #limit = 10
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
        
    return page



@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')



def question_details(request, id):
    #if request.method == "POST": 
        #return add_answer(request)
    
    question = get_object_or_404(Question, id=int(id))
        
    if request.method == "POST":
        form = AnswerForm(request.POST, _question=question)
        if form.is_valid():
            answer = form.save()
            url = answer.question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question' : question.id})
        
    return render(request, 'question_details.html', {
        'question': question,
        'answers': question.answer_set.all(),
        'form': form,
        #'POST_url': request.path,
        'webpage_title': 'Question details',
    })



@require_GET
def questions(request):
    page = paginate(request, Question.objects.order_by('-id'))
    return render(request, 'questions.html', {
        'page': page,
        'baseurl': '/?page=',
        'webpage_title': 'New questions',
    })
    
    

@require_GET    
def popular_questions(request):
    page = paginate(request, Question.objects.order_by('-rating'))
    return render(request, 'questions.html', {
        'page': page,
        'baseurl': '/popular/?page=',
        'webpage_title': 'Popular questions',
    })    



def new_question(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            #return HttpResponse(str(form.cleaned_data))
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'new_question.html', {
        'form': form,
        'webpage_title': 'New question',
    })



@require_POST
def add_answer(request): #stub for test
    return HttpResponse('OK')
    #return HttpResponse(str(request.POST.get('question', 'X')))
    
    
    
def signup(request) :
	if request.method == "POST" :
		form = SignupForm(request.POST)
		if form.is_valid() :
			user = form.save()
			user = form.loginUser()
			#user = authenticate(username=request.POST['username'], password=request.POST['password'])
			login(request, user)
			return HttpResponseRedirect("/")
	else :
		form = SignupForm()
	return render(request, 'ask_add.html', {
		'form' : form,
	})



def signup(request) :
	if request.method == "POST" :
		form = SignupForm(request.POST)
		if form.is_valid() :
			print("POST!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			print("username: " + request.POST.get("username") + "!")
			print("password: " + request.POST.get("password") + "!")
			print("email: " + request.POST.get("email") + "!")
			form.set_password(request.POST.get("password"))
			user = form.save()
			print("SAVE USER!!!!!!!!!!!!!!!!!!!!!!!")
			print("username: " + user.username + " !")
			print("password: " + user.password + " !")
			print("email: " + user.email + " !")
			form.loginUser(request)
			return HttpResponseRedirect("/")
	else :
		form = SignupForm()
	return render(request, 'ask_add.html', {
		'form' : form,
	})
	
def login(request) :
	if request.method == "POST" :
		form = LoginForm(request.POST)
		if form.is_valid() :
			form.set_password(request.POST.get("password"))
			user = form.loginUser(request)
			return HttpResponseRedirect("/")
	else :
		form = LoginForm()
	return render(request, 'ask_add.html', {
		'form' : form,
	})

