from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Artiles
from django.views.generic import DetailView


def news_home(request):
    # news = Artiles.objects.all()
    news = Artiles.objects.order_by('-date')  # [:2]
    # сортировка по алфавиту если поставить минус то будет в обратном порядке
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details.html'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Not right'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
