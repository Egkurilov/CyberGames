from django.db import models


# Create your models here.

# https://www.mindmeister.com/ru/2074249033?t=69WSyEgMWV

# db USER
class USER(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    fio = models.CharField(max_length=255)
    tab_number = models.CharField(max_length=255)
    game_account = models.CharField(max_length=255)
    game = models.CharField(max_length=255)

    def __str__(self):
        return self.name[:50]


class GAMES(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name[:50]
# db TEAMS

# db TOURNAMENT

# db MAIL
