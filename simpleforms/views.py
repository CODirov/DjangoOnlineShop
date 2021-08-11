from simpleforms.forms import NewsForm
from django.shortcuts import render, redirect

from django.urls import reverse

from simpleforms.models import News


def index(request):
    news = News.objects.all()
    context = {
        "news": news
    }
    return render(request, "simpleforms/list.html", context)

def create(request):
    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("news-list"))

    context = {
        "form": form
    }

    return render(request, "simpleforms/create.html", context)

def update(request, pk):
    news = News.objects.filter(id=pk)
    if not news.exists():
        return redirect(reverse("news-list"))
    else:
        news = news.first()

    form = NewsForm(instance=news)

    if request.method == "POST":
        news = NewsForm(request.POST, request.FILES, instance=news)
        if news.is_valid():
            news.save()
            return redirect(reverse("news-list"))

    context = {
        "form": form
    }

    return render(request, "simpleforms/update.html", context)


def delete(request, pk):
    try:
        news = News.objects.get(id=pk)
        news.delete()
    except News.DoesNotExist:
        pass
    
    return redirect(reverse("news-list"))
