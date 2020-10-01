import profile

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.contrib.auth import authenticate, login

from .forms import LoginForm, Resetform,ProfileForm

from .models import Question, Choice, Profile
from django.http import Http404, request
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#
#     context = {'latest_question_list': latest_question_list}
#     return render(request, template, context)
#
# def detail(request, question_id):
#     try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("question doesnot exist")
#     return render(request,'polls/details.html',{'question':question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
from django.shortcuts import render
@login_required
def index(request):
    # if request.user.is_authenticated:
    print(request.user)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    profileform =ProfileForm(request.POST or None)
    context = {
        'latest_question_list': latest_question_list,
        'form': profileform,

    }
    return HttpResponse(template.render(context, request))




def login_page(request):
    print(request.user)
    template = loader.get_template('polls/login.html')
    loginform = LoginForm
    context = {
        'form': loginform,
    }
    return HttpResponse(template.render(context, request))


def logout_page(request):
    logout(request)
    template = loader.get_template('polls/logout.html')
    return HttpResponse(template.render({}, request))




from django.contrib import messages


def login_handle(request):
    print(request.user)
    form = LoginForm(request.POST)
    print(form.data)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'username or password not correct')
            return redirect('/login')
    else:
        messages.error(request, 'form not valid')
        return redirect('/login')



@login_required
def set_password(request):
    print(request.user)
    template = loader.get_template('polls/setpassword.html')
    resetform = Resetform
    context = {
        'form': resetform,

    }
    return HttpResponse(template.render(context, request))

def password_handle(request):
    print(request.user)
    form = Resetform(request.POST)
    print(form.data)
    user = request.user
    if form.is_valid():
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']
        if password == confirm_password:
            user.set_password(confirm_password)
            user.save()
            return redirect("/")
        else:
            messages.error(request, '  confirm password  not match ')
            return redirect('/setpassword')
    else:
        messages.error(request, '  Not a valid password ')
        return redirect('/setpassword')


# def render_to_response(param, param1):
#     pass
def profile(request):
    # profile(request)
    template = loader.get_template('polls/profile.html')
    return HttpResponse(template.render({}, request))


def profile_handle(request):
    print(request.user)
    form = ProfileForm(request.POST)
    user = request.user
    user.profile.testy()
    if form.is_valid():
        # profile_pic = form.cleaned_data['profile_pic']
        # birth_date = form.cleaned_data['birth_date']
        mobile_number = form.cleaned_data['mobile_number']
        address = form.cleaned_data['address']
        country = form.cleaned_data['country']
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
        profile = user.profile
        profile.mobile_number = mobile_number
        profile.address = address
        profile.save()
        return redirect("/profile")
    else:
        print(form.errors)
        messages.error(request, '  Not a valid ')
        return redirect('/')

    # user = request.user
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST)
    #     if form.is_valid():
    #         first_name= form.save(commit=False)
    #         first_name.user = request.user # Set the user object here
    #         first_name.save()
    #         return redirect('/')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())




class ResultsView(generic.DetailView):
    model=Question
    template_name = 'polls/results.html'


