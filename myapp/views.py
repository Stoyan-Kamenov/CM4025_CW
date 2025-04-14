from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Stories, Ratings
from .forms import StoryForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def library(request):
    stories = Stories.objects.all()
    return render(request, 'library.html', {'stories': stories})

def addStory(request):
    submitted = False
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            if request.user.is_authenticated:
                story.user = request.user
            else:
                story.user = None
            story.save()
            return HttpResponseRedirect('/addStory?submitted=True')
    else:
        form = StoryForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'addStory.html', {'form': form, 'submitted': submitted})

def manageStory(request):
    return render(request, 'manageStory.html')

def account(request):
    return render(request, 'account.html')

def rankings(request):
    return render(request, 'rankings.html')

def rate_story(request, story_id):
    if request.method == 'POST':
        story = get_object_or_404(Stories, storyId=story_id)
        rating_value = int(request.POST.get('rating', 0))
        if 1 <= rating_value <= 5:  
            Ratings.objects.create(storyId=story, rating=rating_value)
    return redirect('library') 