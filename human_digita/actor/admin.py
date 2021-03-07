from django.contrib import admin

# Register your models here.
from human_digita.actor.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    autocomplete_fields = ['person']

