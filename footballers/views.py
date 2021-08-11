from footballers.forms import PlayerForm
from django.shortcuts import redirect, render
from django.urls.base import reverse

from .models import Club, Player, Position


def players(request):
    players = Player.objects.all()
    
    context = {
        "players": players
    }

    return render(request, "footballers/players.html", context)

def add_player(request):
    form = PlayerForm()
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("players-list"))

    context = {
        "form": form
    }

    return render(request, "footballers/add_player.html", context)

def update_player(request, pk):
    player = Player.objects.filter(id=pk)
    if not player.exists():
        return redirect(reverse("players-list"))
    else:
        player = player.first()

    form = PlayerForm(instance=player)


    if request.method == "POST":
        player = PlayerForm(request.POST, request.FILES, instance=player)
        if player.is_valid():
            player.save()
        return redirect(reverse("players-list"))

    context = {
        "form": form
    }

    return render(request, "footballers/update_player.html", context)

def delete_player(request, pk):
    try:
        player = Player.objects.get(id=pk)
        player.delete()
    except player.DoesNotExist:
        pass

    return redirect(reverse("players-list"))