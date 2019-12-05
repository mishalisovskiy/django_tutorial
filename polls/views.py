from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': q})


def results(request, question_id):
    response = "you're looking at the results of question no {}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse("You're looking at the question no. {}".format(question_id))
