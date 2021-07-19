from django.contrib import admin
from django.urls import path, include
from store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("store/", include("store.urls")),
]
