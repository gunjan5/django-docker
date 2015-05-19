from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    f_p = models.ForeignKey(User, related_name="games_f_p")
    s_p = models.ForeignKey(User,related_name="games_s_p")
    n_to_m = models.ForeignKey(User,related_name="games_to_m")
    s_time = models.DateTimeField(auto_now_add=True)
    l_active = models.DateTimeField(auto_now=True)
    

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300)
    game = models.ForeignKey(Game)
