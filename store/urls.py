from django.urls import path
from .views import *


urlpatterns = [
    path("", home, name="bosh-sahifa"),
    path("product/<slug:slug>/", product_detail, name="product-detail")
]