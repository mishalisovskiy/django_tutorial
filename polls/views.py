from django.http import HttpResponse

from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You're looking at the question no. {}".format(question_id))


def results(request, question_id):
    response = "you're looking at the results of question no {}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse("You're looking at the question no. {}".format(question_id))
