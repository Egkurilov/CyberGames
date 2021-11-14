from datetime import datetime

from django.db import models


# Create your models here.

# https://www.mindmeister.com/ru/2074249033?t=69WSyEgMWV

# db USER
class USER(models.Model):
    id = models.BigAutoField(primary_key=True)
    nickname = models.CharField(max_length=255, db_index=True)
    fio = models.CharField(max_length=255)
    tab_number = models.CharField(max_length=255)
    game_account = models.CharField(max_length=255)
    game = models.ForeignKey('GAME', default=None, null=True, on_delete=models.CASCADE)
    register_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname[:50]

    class Meta:
        db_table = 'USERS'


# db GAME
class GAME(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(default=None, upload_to='images/game/')

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'GAMES'


# db TEAMS
class TEAM(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(default=None, upload_to='images/team/')
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
    logo = models.ImageField(default=None, upload_to='images/tournament/')
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

# TODO db MAIL
