from django.db import models


# Create your models here.

# https://www.mindmeister.com/ru/2074249033?t=69WSyEgMWV

# db USER
class USER(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    fio = models.CharField(max_length=255)
    tab_number = models.CharField(max_length=255)
    game_account = models.CharField(max_length=255)
    game = models.ForeignKey('GAMES', default=None, null=True, on_delete=models.CASCADE)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'USERS'


# db GAMES
class GAMES(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'GAMES'


# db TEAMS
class TEAMS(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'TEAMS'


# db TOURNAMENT
class TOURNAMENT(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name[:50]

    class Meta:
        db_table = 'TOURNAMENT'

# TODO db MAIL
