from django.contrib import admin

# Register your models here.
from .models import Event, Photo

admin.site.register(Event)
admin.site.register(Photo)