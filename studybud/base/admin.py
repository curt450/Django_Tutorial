from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message

admin.site.Register(Room)
admin.site.Register(Messages)
admin.site.Register(Topic)