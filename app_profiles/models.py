from django.db import models


class USER(models.Model):
    id = models.BigAutoField(primary_key=True)
    nickname = models.CharField(max_length=255, db_index=True)
    password = models.CharField(max_length=255, default=None)
    first_name = models.CharField(max_length=255, default=None)
    second_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField(null=True, max_length=255)
    tab_number = models.CharField(max_length=255)
    game_account = models.CharField(max_length=255)
    game = models.ForeignKey('sber_games.GAME', default=None, null=True, on_delete=models.CASCADE)
    register_date = models.DateTimeField(auto_now_add=True)
    teams = models.ForeignKey('sber_games.TEAM', default=None, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname[:50]

    class Meta:
        db_table = 'USER'


class TEST(models.Model):
    test = models.CharField(max_length=255)
