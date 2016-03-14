try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse, NoReverseMatch
from django.http import Http404, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

try:
    from stepic_web.ask.qa.models import Question, Answer
    from stepic_web.ask.qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
except ImportError:
    import sys
    sys.path.append("/home/box")
    from web.ask.qa.models import Question, Answer
    from web.ask.qa.forms import AskForm, AnswerForm, SignupForm, LoginForm

LIMIT = 10


def panginate(request, qs):
    try:
        page_num = int(request.GET.get("page", 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, LIMIT)

    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page_num, page


def build_url(name, url_params):
    try:
        url = reverse(name)
    except NoReverseMatch:
        url = name

    if url_params:
        url += '?' + urlencode(url_params)
    return url


def get_questions(request, question_type):
    new_questions = Question.objects.get_questions_by_type(question_type)
    page_num, page = panginate(request, new_questions)

    next_page_ref = build_url(question_type, {"page": page_num+1}) if page.has_next() else request.path
    prev_page_ref = build_url(question_type, {"page": page_num-1}) if page.has_previous() else request.path

    return render(request, "question_list.html", {"questions": page.object_list, "next_page_ref": next_page_ref,
                                                  "prev_page_ref": prev_page_ref})


#@login_required
def get_current_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    user = request.user
    if request.method == "POST":
        text = request.POST["text"]
        question = request.POST["question"]
        form = AnswerForm(user, text=text, question=question)
        if form.is_valid():
            form.save()
    else:
        form = AnswerForm(user, question=question_id)
    answers = Answer.objects.filter(question=question)
    c = {"question": question, "answers": answers, "form": form}
    return render(request, "current_question.html", c)


#@login_required
def ask_question(request):
    user = request.user
    if request.method == "POST":
        text = request.POST["text"]
        title = request.POST["title"]
        form = AskForm(user, text=text, title=title)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm(user)
    c = {"form": form}
    return render(request, "ask_question.html", c)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/")
    else:
        form = SignupForm()
    c = {"form": form}
    return render(request, "signup.html", c)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    c = {"form": form}
    return render(request, "signup.html", c)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
