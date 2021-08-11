from schoolforms.forms import StaffForm
from django.shortcuts import redirect, render
from django.urls.base import reverse

from .models import Staff, Rank


def list(request):
    staff = Staff.objects.all()
    context = {
        "staff": staff,
    }
    return render(request, "schoolforms/staff_list.html", context)


def add_stuff(request):
    form = StaffForm()
    if request.method=="POST":
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("stuff-list"))

    context = {
        "form": form
    }

    return render(request, "schoolforms/add_staff.html", context)


def update_stuff(request, pk):
    staff = Staff.objects.filter(id=pk)
    if not staff.exists():
        return redirect(reverse("news-list"))
    else:
        staff = staff.first()

    form = StaffForm(instance=staff)

    if request.method == "POST":
        staff = StaffForm(request.POST, request.FILES, instance=staff)
        if staff.is_valid():
            staff.save()
            return redirect(reverse("stuff-list"))

    context = {
        "form": form
    }

    return render(request, "schoolforms/update.html", context)


def delete_stuff(request, pk):
    try:
        staff = Staff.objects.get(id=pk)
        staff.delete()
    except Staff.DoesNotExist:
        pass

    return redirect(reverse("stuff-list"))