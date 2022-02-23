from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print("line5")
    return HttpResponse("<h2>hello world</h2>")

