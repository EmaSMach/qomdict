from django.shortcuts import render

from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.
from .models import Word


class HomeView(TemplateView):
    template_name = "dictionary/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        word = self.request.GET.get('word')
        if word is None:
            buscando = False
        else:
            word = word.strip().lower()
            buscando = True
        # context['words'] = Word.objects.all()
        if word:
            word = Word.objects.filter(qom=word).first()
            context['word'] = word
        context['buscando'] = buscando
        return context
        

class WordListView(ListView):
    model = Word
    template_name = "dicionary/word_list.html"


class WordDetailView(DetailView):
    model = Word


def search_word(request, word):
    word = Word.objects.get(qom=word)
    context = {'word': word or None}
    return render(request, template_name='dicionary/index.html', context=context)
