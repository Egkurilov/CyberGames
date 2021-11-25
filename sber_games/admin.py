from django.contrib import admin
from sber_games.models import GAME, TOURNAMENT, TEAM
from app_profiles.models import USER

# Register your models here.


@admin.register(USER)
class sber_gamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'first_name', 'second_name', 'last_name', 'email', 'status',)


@admin.register(GAME)
class sber_gamesAdmin(admin.ModelAdmin):
    pass


@admin.register(TOURNAMENT)
class sber_gamesAdmin(admin.ModelAdmin):
    list_filter = ('game_id', 'team_member_id', 'user_member_id', )


@admin.register(TEAM)
class sber_gamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'members_id', 'game_id', 'capitan', 'tournaments_id', 'status',)
    list_filter = ('game_id', 'tournaments_id', 'members_id', )




# @admin.register(TOURNEY_MEMBER)
# class sber_gamesAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(TEAM_MEMBER)
# class sber_gamesAdmin(admin.ModelAdmin):
#     pass
