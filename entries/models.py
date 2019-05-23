from django.db import models
 #answer = models.PositiveIntegerField(default=0)
# Create your models here.
class Teams(models.Model):
	team_name = models.CharField(max_length=100)
	def __str__(self):
    		return self.team_name
class Fixtures(models.Model):
	id = models.AutoField(primary_key=True)
	home_team = models.ForeignKey(Teams, models.CASCADE, related_name="games_as_team1", null=True)
	away_team = models.ForeignKey(Teams, models.CASCADE, related_name="games_as_team2", null=True)
	game_week = models.PositiveIntegerField(default=0)

class Question(models.Model):
    #TRUE = 'TRUE'
    #FALSE = 'FALSE'
    #Q_CHOICES = [(TRUE, 'True'), (FALSE, 'False')]
	#answer = models.CharField(max_length=10, choices=Q_CHOICES, default=TRUE
	#question_text = models.CharField(max_length=200)
    #game_week = models.PositiveIntegerField(default=0)
    TRUE = 'TRUE'
    FALSE = 'FASLE'
    Q_CHOICES = [
        (TRUE, 'True'),
        (FALSE, 'False'),
    ]
    answer = models.CharField(
        max_length=5,
        choices=Q_CHOICES,
        default=TRUE,
    )
    question_text = models.CharField(max_length=200, default="test")
    game_week = models.PositiveIntegerField(default=0)
	
class Players(models.Model):
	player_fname = models.CharField(max_length=100)
	player_lname = models.CharField(max_length=100)
	player_team = models.ForeignKey(Teams, on_delete=models.CASCADE)
		