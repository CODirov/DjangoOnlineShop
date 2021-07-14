from django.contrib import admin
from django.urls import path, include
from store.views import home, single_music


urlpatterns = [
    path('admin/', admin.site.urls),
    path("store/", include("store.urls"))
]
