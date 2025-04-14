from django.contrib import admin
from .models import Stories
from .models import Ratings

admin.site.register(Stories)
admin.site.register(Ratings)