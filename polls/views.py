from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Its me.")
 
# Create your views here.
