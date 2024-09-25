from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from polls.models import Question, Choice

def index(request):
    questions = Question.objects.all()
    response = "<ol>"
    for question in questions:
        response += f"<li>{question.question_text}</li>"
    response += "</ol>"
    return HttpResponse(response)