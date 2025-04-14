from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def library(request):
    return render(request, 'library.html')

def addStory(request):
    return render(request, 'addStory.html')

def manageStory(request):
    return render(request, 'manageStory.html')

def account(request):
    return render(request, 'account.html')

def leaderboards(request):
    return render(request, 'leaderboards.html')
