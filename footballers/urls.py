from django.urls import path

from . import views

urlpatterns = [
    path("", views.players, name="players-list"),
    path("add_player/", views.add_player, name="add-player"),
    path("update_player/<int:pk>/", views.update_player, name="update-player"),
    path("delete_player/<int:pk>/", views.delete_player, name="delete-player")
]