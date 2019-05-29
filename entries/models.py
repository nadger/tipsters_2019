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
	player_name = models.CharField(max_length=100)
	player_team = models.ForeignKey(Teams, on_delete=models.CASCADE)

#needs work
class Results(models.Model):
	userid = models.CharField(max_length=100)
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
	
		