from django.shortcuts import render

# Create your views here.
from .models import Question, Choice

def index(request):
    render(request, 'polls/index.html')