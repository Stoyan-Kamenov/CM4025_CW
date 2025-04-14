from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('library/', views.library, name='library'),
    path('addStory/', views.addStory, name='addStory'),
    path('manageStory/<story_id>', views.manageStory, name='manageStory'),
    path('account/', views.account, name='account'),
    path('stories/', views.storiesList, name='storiesList'),
    path('rateStory/<uuid:story_id>/', views.rateStory, name='rateStory'),
    path('deleteStory/<uuid:story_id>/', views.deleteStory, name='deleteStory'),
    path('account/delete/', views.delete_account, name='delete_account'),
    path('story/<uuid:story_id>/', views.viewStory, name='viewStory'),

]