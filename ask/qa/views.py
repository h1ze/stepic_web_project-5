from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from qa.models import *
from django.core.paginator import Paginator, EmptyPage



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



def test(request, *args, **kwargs):
    return HttpResponse('OK')
    
def question_details(request, id):
    question = get_object_or_404(Question, id=int(id))
    return render(request, 'question_details.html', {
        'question': question,
        'answers': question.answer_set.all()
    })



def questions(request):
    page = paginate(request, Question.objects.order_by('-id'))
    #return HttpResponse('OK ' + str(questions_page.number))
    return render(request, 'questions.html', {
        'page': page,
        'baseurl': '/?page=',
        'webpage_title': 'stepic-web New questions',
    })
    
    
    
def popular_questions(request):
    page = paginate(request, Question.objects.order_by('-rating'))
    return render(request, 'questions.html', {
        'page': page,
        'baseurl': '/popular/?page=',
        'webpage_title': 'stepic-web Popular questions',
    })    
    
    
    
    
    
    
    
    
    
