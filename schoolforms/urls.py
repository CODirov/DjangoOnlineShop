from django.urls import path

from . import views

urlpatterns = [
    path("", views.list, name="stuff-list"),
    path("add_stuff/", views.add_stuff, name="add-stuff"),
    path("update_stuff/<int:pk>/", views.update_stuff, name="update-stuff"),
    path("delete_stuff/<int:pk>/", views.delete_stuff, name="delete-stuff"),
]