from datetime import datetime

from django.db import models
import uuid


# Create your models here.

# https://www.mindmeister.com/ru/2074249033?t=69WSyEgMWV

# db USER
# class USER(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     nickname = models.CharField(max_length=255, db_index=True)
#     password = models.CharField(max_length=255, default=None)
#     first_name = models.CharField(max_length=255, default=None)
#     second_name = models.CharField(max_length=255, default=None)
#     last_name = models.CharField(max_length=255, default=None)
#     email = models.EmailField(null=True, max_length=255)
#     tab_number = models.CharField(max_length=255)
#     game_account = models.CharField(max_length=255)
#     game = models.ForeignKey('GAME', default=None, null=True, on_delete=models.CASCADE)
#     register_date = models.DateTimeField(auto_now_add=True)
#     status = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.nickname[:50]
#
#     class Meta:
#         db_table = 'USERS'


# db GAME
class GAME(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(default=None, upload_to='sber_games/images/game/')

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'GAMES'


# db TEAMS
class TEAM(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(default=None, upload_to='sber_games/images/team/')
    game = models.ForeignKey('GAME', default=None, null=True, on_delete=models.CASCADE)
    members = models.CharField(max_length=2555)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'TEAMS'


# db TOURNAMENT
class TOURNAMENT(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey('GAME', default=None, null=True, on_delete=models.CASCADE)
    logo = models.ImageField(default=None, upload_to='sber_games/images/tournament/')
    created_date = models.DateTimeField(default=datetime.now)
    start_date = models.DateTimeField()
    members = models.CharField(max_length=2555, default=None)
    prize = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255, default=1)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'TOURNAMENTS'


class PARTICIPANTS_UTournament(models.Model):
    user = models.ForeignKey('app_profiles.USER', default=None, null=True, on_delete=models.CASCADE)
    tournament = models.ForeignKey('TOURNAMENT', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ParticipantsUserToTournament'


class PARTICIPANTS_UTeam(models.Model):
    user = models.ForeignKey('app_profiles.USER', default=None, null=True, on_delete=models.CASCADE)
    teams = models.ForeignKey('TEAM', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ParticipantsUserToTeam'

# TODO db MAIL
