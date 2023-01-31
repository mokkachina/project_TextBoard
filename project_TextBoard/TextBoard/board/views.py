from django.shortcuts import render
from django.views.generic import ListView

from .models import Article


class TextBoard(ListView):
    model = Article

    template_name = 'board.html'
    context_object_name = 'board'
    paginate_by = 10
