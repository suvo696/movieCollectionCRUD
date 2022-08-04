from django.contrib import admin

# Register your models here.
from .models import Movie, Collection, Counter

admin.site.register(Movie)
admin.site.register(Collection)
admin.site.register(Counter)