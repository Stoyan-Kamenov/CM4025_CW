from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Stories, Ratings
from .forms import StoryForm
import random


# Go to Home
def home(request):
    stories = Stories.objects.filter(isPublic=True)
    random_story = random.choice(stories) if stories.exists() else None
    return render(request, 'home.html', {'random_story': random_story})

# Go to Library
def library(request):
    stories = Stories.objects.all()
    return render(request, 'library.html', {'stories': stories})

# Add Story
def addStory(request):
    submitted = False
    if request.method == 'POST':
        form = StoryForm(request.POST, user_authenticated=request.user.is_authenticated)
        if form.is_valid():
            story = form.save(commit=False)
            if request.user.is_authenticated:
                story.user = request.user
            else:
                story.user = None
            story.save()
            return HttpResponseRedirect('/addStory?submitted=True')
    else:
        form = StoryForm(user_authenticated=request.user.is_authenticated)
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'addStory.html', {'form': form, 'submitted': submitted})

# Update Story
def manageStory(request, story_id):
    story = get_object_or_404(Stories, storyId=story_id)
    if request.method == 'POST':
        form = StoryForm(request.POST, instance=story, user_authenticated=request.user.is_authenticated)
        if form.is_valid():
            form.save()
            return redirect('storiesList')  # Redirect to the stories list after saving
    else:
        form = StoryForm(instance=story, user_authenticated=request.user.is_authenticated)
    return render(request, 'manageStory.html', {'form': form, 'story': story})

# Delete Story
def deleteStory(request, story_id):
    story = Stories.objects.get(storyId=story_id)
    story.delete()
    return redirect('storiesList')

# View Story
def viewStory(request, story_id):
    story = get_object_or_404(Stories, storyId=story_id)
    return render(request, 'viewStory.html', {'story': story})

# Account
def account(request):
    return render(request, 'account.html')

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  
        return redirect('home')  
    return redirect('account')

# Story List
@login_required
def storiesList(request):
    user_stories = Stories.objects.filter(user=request.user) 
    return render(request, 'storiesList.html', {'stories': user_stories})

# Rating
def rateStory(request, story_id):
    if request.method == 'POST':
        story = get_object_or_404(Stories, storyId=story_id)
        rating_value = int(request.POST.get('rating', 0))
        if 1 <= rating_value <= 5:  
            Ratings.objects.create(storyId=story, rating=rating_value)
    return redirect('library') 