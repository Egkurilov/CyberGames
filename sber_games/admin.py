from django.contrib import admin
from sber_games.models import GAME, TOURNAMENT, TEAM
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


# @admin.register(PARTICIPANTS_UTournament)
# class sber_gamesAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(PARTICIPANTS_UTeam)
# class sber_gamesAdmin(admin.ModelAdmin):
#     pass
