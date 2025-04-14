from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.library, name='library'),
    path('addStory/', views.addStory, name='addStory'),
    path('manageStory/', views.manageStory, name='manageStory'),
    path('account/', views.account, name='account'),
    path('leaderboards/', views.leaderboards, name='leaderboards')
]