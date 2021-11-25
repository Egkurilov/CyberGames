from datetime import datetime

from django.db import models
import uuid


# Create your models here.

# https://www.mindmeister.com/ru/2074249033?t=69WSyEgMWV


# db GAME
class GAME(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(default=None, upload_to='sber_games/images/game/')

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'GAMES'


class MATCH(models.Model):
    # team1
    team1_name = models.CharField(max_length=255)
    team1_logo = models.CharField(max_length=255)
    # team2
    team2_name = models.CharField(max_length=255)
    team2_logo = models.CharField(max_length=255)

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'MATCH'

# db TEAMS
class TEAM(models.Model):
    name = models.CharField(max_length=255)
    capitan = models.CharField(max_length=255, default=None)
    logo = models.ImageField(default=None, upload_to='sber_games/images/team/')
    game = models.ForeignKey('GAME', default=None, null=True, on_delete=models.CASCADE)
    members = models.ForeignKey('app_profiles.USER', default=None, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    tournament = models.ForeignKey('TOURNAMENT', default=None, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'TEAMS'


# db TOURNAMENT
class TOURNAMENT(models.Model):
    name = models.CharField(max_length=255)
    game = models.ForeignKey('GAME', blank=True, null=True, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='sber_games/images/tournament/')
    created_date = models.DateTimeField(default=datetime.now)
    start_date = models.DateTimeField()
    prize = models.CharField(max_length=255)
    chat_id = models.CharField(max_length=255, default=1)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'TOURNAMENTS'


class TEAM_MEMBER(models.Model):
    user = models.ForeignKey('app_profiles.USER', default=None, null=True, on_delete=models.CASCADE)
    teams = models.ForeignKey('TEAM', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TEAM_MEMBER'


class TOURNEY_MEMBER(models.Model):
    teams = models.ForeignKey('TEAM', default=None, null=True, on_delete=models.CASCADE)
    tournament = models.ForeignKey('TOURNAMENT', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'TOURNEY_MEMBER'

# TODO db MAIL
