from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import transaction

from simpleforms.forms import DirectorForm
from simpleforms.models import Filial
from .utils import parse_date_time


def index(request):
    filials = Filial.objects.all()
    context = {
    "filials": filials
    }
    return render(request, "simpleforms/list.html", context)

# def create(request):
#     if request.method == "POST":
#         title = request.POST.get("title", None)
#         date = request.POST.get("date", None)
#         time = request.POST.get("time", None)
#         director = request.POST.get("director", None)
#         experience = request.POST.get("experience", None)

#         with transaction.atomic():
#             f = Filial(title=title, established_at=parse_date_time(date, time))
#             f.save()

#             d = Director(fullname=director, experience=experience, filial=f)
#             d.save()

#         return redirect(reverse("news-list"))
#     context = {
#     }
def create(request):
    form = DirectorForm()
    if request.method=="POST":
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("news-list"))

    context = {
        "form": form
    }

    return render(request, "simpleforms/create.html", context)

def update(request, pk):
    try:
        filial = Filial.objects.get(id=pk)
        date = filial.established_at.strftime("%Y-%m-%d")
        time = filial.established_at.strftime("%H:%M")
    except:
        return redirect(reverse("news-list"))

    if request.method == "POST":
        title = request.POST.get("title", None)
        date = request.POST.get("date", None)
        time = request.POST.get("time", None)
        director = request.POST.get("director", None)
        experience = request.POST.get("experience", None)

        filial.title = title
        filial.established_at = parse_date_time(date, time)
        filial.director.fullname = director
        filial.director.experience = experience
        filial.save()
        filial.director.save()

        return redirect(reverse("news-list"))

    context = {
        "filial": filial,
        "date": date,
        "time": time
    }

    return render(request, "simpleforms/update.html", context)


def delete(request, pk):
    try:
        Filial.objects.filter(id=pk).delete()
    except:
        pass
    return redirect(reverse("news-list"))
