from django.shortcuts import render

from news.models import News


def home_page(request):
    news_all = News.objects.all()
    context = {
        'news': news_all,
    }
    return render(request, 'home.html', context)


def news_detail_view(request, id):
    news = News.objects.get(id=id)
    context = {
        'news': news
    }
    return render(request, 'news.detail.html', context)
