from django.contrib import admin
from sber_games.models import GAME, TOURNAMENT, TEAM, TOURNEY_MEMBER, TEAM_MEMBER
from app_profiles.models import USER

# Register your models here.


@admin.register(USER)
class sber_gamesAdmin(admin.ModelAdmin):
    pass


@admin.register(GAME)
class sber_gamesAdmin(admin.ModelAdmin):
    pass


@admin.register(TOURNAMENT)
class sber_gamesAdmin(admin.ModelAdmin):
    pass


@admin.register(TEAM)
class sber_gamesAdmin(admin.ModelAdmin):
    pass


@admin.register(TOURNEY_MEMBER)
class sber_gamesAdmin(admin.ModelAdmin):
    pass


@admin.register(TEAM_MEMBER)
class sber_gamesAdmin(admin.ModelAdmin):
    pass
