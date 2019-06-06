from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
	user_teamname=models.CharField(max_length=100,null=True)
	pass

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
	player_name = models.CharField(max_length=100)
	player_team = models.ForeignKey(Teams, on_delete=models.CASCADE)

class configdata(models.Model):
	current_gw = models.PositiveIntegerField(default=0)
	current_season = models.PositiveIntegerField(default=2019)

class entry_data(models.Model):
	entry_gw = models.PositiveIntegerField(default=0)
	entry_season = models.PositiveIntegerField(default=2019)
	team_id = models.PositiveIntegerField(default=2019)
	score_home_fix1 = models.PositiveIntegerField(default=0)
	score_home_fix2 = models.PositiveIntegerField(default=0)
	score_home_fix3 = models.PositiveIntegerField(default=0)
	score_home_fix4 = models.PositiveIntegerField(default=0)
	score_home_fix5 = models.PositiveIntegerField(default=0)
	score_home_fix6 = models.PositiveIntegerField(default=0)
	score_home_fix7 = models.PositiveIntegerField(default=0)
	score_home_fix8 = models.PositiveIntegerField(default=0)
	score_home_fix9 = models.PositiveIntegerField(default=0)
	score_home_fix10 = models.PositiveIntegerField(default=0)
	score_away_fix1 = models.PositiveIntegerField(default=0)
	score_away_fix2 = models.PositiveIntegerField(default=0)
	score_away_fix3 = models.PositiveIntegerField(default=0)
	score_away_fix4 = models.PositiveIntegerField(default=0)
	score_away_fix5 = models.PositiveIntegerField(default=0)
	score_away_fix6 = models.PositiveIntegerField(default=0)
	score_away_fix7 = models.PositiveIntegerField(default=0)
	score_away_fix8 = models.PositiveIntegerField(default=0)
	score_away_fix9 = models.PositiveIntegerField(default=0)
	score_away_fix10 = models.PositiveIntegerField(default=0)
	score_away_fix11 = models.PositiveIntegerField(default=0)
	score_tg = models.PositiveIntegerField(default=0)
	entry_q1 = models.CharField(max_length=5)
	entry_q2 = models.CharField(max_length=5)
	entry_q3 = models.CharField(max_length=5)
	entry_q4 = models.CharField(max_length=5)
	entry_q5 = models.CharField(max_length=5)
	entry_q6 = models.CharField(max_length=5)
	entry_q7 = models.CharField(max_length=5)
	entry_q8 = models.CharField(max_length=5)
	entry_q9 = models.CharField(max_length=5)
	entry_q10 = models.CharField(max_length=5)
	entry_player1 = models.CharField(max_length=20)
	entry_player2 = models.CharField(max_length=20)
	entry_player3 = models.CharField(max_length=20)
	entry_player4 = models.CharField(max_length=20)

	"""docstring for entry_data"""
	def __init__(self, arg):
		super(entry_data, self).__init__()
		self.arg = arg

				

#needs work
class Results(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
	season = models.PositiveIntegerField(default=0)
	gw1score = models.PositiveIntegerField(default=0)
	gw2score = models.PositiveIntegerField(default=0)
	gw3score = models.PositiveIntegerField(default=0)
	gw4score = models.PositiveIntegerField(default=0)
	gw5score = models.PositiveIntegerField(default=0)
	gw6score = models.PositiveIntegerField(default=0)
	gw7score = models.PositiveIntegerField(default=0)
	gw8score = models.PositiveIntegerField(default=0)
	gw9score = models.PositiveIntegerField(default=0)
	gw10score = models.PositiveIntegerField(default=0)
	gw11score = models.PositiveIntegerField(default=0)
	gw12score = models.PositiveIntegerField(default=0)
	gw13score = models.PositiveIntegerField(default=0)
	gw14score = models.PositiveIntegerField(default=0)
	gw15score = models.PositiveIntegerField(default=0)
	gw16score = models.PositiveIntegerField(default=0)
	gw17score = models.PositiveIntegerField(default=0)
	gw18score = models.PositiveIntegerField(default=0)
	gw19score = models.PositiveIntegerField(default=0)
	gw20score = models.PositiveIntegerField(default=0)
	gw21score = models.PositiveIntegerField(default=0)
	gw22score = models.PositiveIntegerField(default=0)
	gw23score = models.PositiveIntegerField(default=0)
	gw24score = models.PositiveIntegerField(default=0)
	gw25score = models.PositiveIntegerField(default=0)
	gw26score = models.PositiveIntegerField(default=0)
	gw27score = models.PositiveIntegerField(default=0)
	gw29score = models.PositiveIntegerField(default=0)
	gw29score = models.PositiveIntegerField(default=0)
	gw30score = models.PositiveIntegerField(default=0)
	gw31score = models.PositiveIntegerField(default=0)
	gw32score = models.PositiveIntegerField(default=0)
	gw33score = models.PositiveIntegerField(default=0)
	gw34score = models.PositiveIntegerField(default=0)
	gw35score = models.PositiveIntegerField(default=0)
	gw36score = models.PositiveIntegerField(default=0)
	gw37score = models.PositiveIntegerField(default=0)
	gw38score = models.PositiveIntegerField(default=0)
	gw39score = models.PositiveIntegerField(default=0)
	gw40score = models.PositiveIntegerField(default=0)
	
		