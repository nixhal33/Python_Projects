from django.shortcuts import render,HttpResponse


# Create your views here.

def home(request):
    # return HttpResponse("This is my first page")
    return render(request, 'base.html')