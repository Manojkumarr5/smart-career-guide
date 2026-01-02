from django.http import HttpResponse

def home(request):
    return HttpResponse("Smart Career Guide Home Page")
