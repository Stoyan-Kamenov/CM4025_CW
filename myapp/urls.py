from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.library, name='library'),
    path('addStory/', views.addStory, name='addStory'),
    path('manageStory/', views.manageStory, name='manageStory'),
    path('account/', views.account, name='account'),
    path('rankings/', views.rankings, name='rankings'),
    path('rate_story/<uuid:story_id>/', views.rate_story, name='rate_story')
]