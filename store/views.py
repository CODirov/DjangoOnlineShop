from django.http import HttpResponse

def home(request):
    return HttpResponse("barcha qo'shiqlar")

def single_music(request):
    return HttpResponse("musiqa")