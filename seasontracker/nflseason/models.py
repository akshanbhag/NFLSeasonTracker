from django.db import models

#Games table
class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    home_team = models.IntegerField()
    away_team = models.IntegerField()
    winner = models.IntegerField()
    date_played = models.DateField()
    week_number = models.IntegerField()

#Teams table
class Teams(models.Model):
    team_id = models.AutoField(primary_key=True)
    division = models.CharField(max_length=50)
    team_name = models.CharField(max_length=100)
    class Meta:
        indexes = [
            models.Index(fields=['team_id'])
        ]

#Players table
class Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team_id = models.IntegerField()

#Team_Record table
class Team_Record(models.Model):
    team_id = models.IntegerField()
    wins = models.IntegerField()
    year = models.IntegerField()
    week_number = models.IntegerField()

#Season table
class Season(models.Model):
    year = models.IntegerField(primary_key=True)
    superbowl_champ = models.CharField(max_length=100)
    MVP = models.CharField(max_length=100)