from django.contrib import admin
from .models import *

class ActorAdmin(admin.ModelAdmin):
    list_display = ("actor_id", "first_name", "last_name", "last_update")

admin.site.register(Actor, ActorAdmin)
admin.site.register(Film)
admin.site.register(Category)
