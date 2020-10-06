from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.
from .models import Word


class HomeView(TemplateView):
    template_name = "dictionary/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['words'] = Word.objects.all()
        return context
        

class WordListView(ListView):
    model = Word
    template_name = "dicionary/word_list.html"
