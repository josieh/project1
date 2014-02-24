#baseball/roster/admin.py

from django.contrib import admin
from roster.models import Player

# Register your models here.

class MembershipInline(admin.TabularInline):
    model = Player

class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    inlines = [
        MembershipInline,
    ]

admin.site.register(Player, PlayerAdmin)

    