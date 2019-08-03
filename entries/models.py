from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime

class CustomUser(AbstractUser):
	comments=models.CharField(max_length=100,null=True)
	teamname=models.CharField(max_length=100,null=True)
	pass

class configdata(models.Model):
	gameweek = models.PositiveIntegerField(default=0)
	season = models.PositiveIntegerField(default=2019)
	gw_deadline = models.DateTimeField(default=datetime.now)
	gw_active = models.BooleanField(default=False)
	gw_closed = models.BooleanField(default=False)
	def __str__(self):
		return '{} / {}'.format(self.gameweek, self.season)
	class Meta:
		verbose_name = 'Game Week Config'
		verbose_name_plural = 'Game Week Config'

class usr_teams(models.Model):
	team_name = models.CharField(max_length=100,null=True)
	team_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="teams", default=0)
	def __str__(self):
		return self.team_name
	class Meta:
		verbose_name = 'user team'
		verbose_name_plural = 'user teams'

class Teams(models.Model):
	team_name = models.CharField(max_length=100)
	def __str__(self):
    		return self.team_name
	class Meta:
		verbose_name = 'team'
		verbose_name_plural = 'teams'

class Fixtures(models.Model):
	home_team = models.ForeignKey(Teams, models.CASCADE, related_name="games_as_team1", null=True)
	away_team = models.ForeignKey(Teams, models.CASCADE, related_name="games_as_team2", null=True)
	game_week = models.ForeignKey(configdata, models.CASCADE, related_name="Fixture_Game_Week")
	fix_weekid = models.PositiveIntegerField(default=0)
	def __str__(self):
		return '{} v {}'.format(self.home_team, self.away_team)
	class Meta:
		verbose_name = 'fixture'
		verbose_name_plural = 'fixtures'

class Question(models.Model):
    question_text = models.CharField(max_length=200, default="test")
    game_week = models.ForeignKey(configdata, models.CASCADE, related_name="Question_Game_Week")
    def __str__(self):
    	return self.question_text


class Answer(models.Model):
	question = models.ForeignKey(Question, models.CASCADE, related_name="Question_Number")
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

class Players(models.Model):
	player_name = models.CharField(max_length=100)
	player_team = models.ForeignKey(Teams, on_delete=models.CASCADE)
	def __str__(self):
		return self.player_name
	class Meta:
		verbose_name = 'player'
		verbose_name_plural = 'players'


class entry_data(models.Model):
	entry_gw = models.ForeignKey(configdata, models.CASCADE, related_name="Entry_Game_Week")
	team_id = models.ForeignKey(usr_teams, models.CASCADE, related_name="Entry_Team")
	fixture_id = models.ForeignKey(Fixtures, models.CASCADE, related_name="Entry_Team", default=0)
	score_home = models.PositiveIntegerField(default=0)
	score_away = models.PositiveIntegerField(default=0)

class entry_data_new(models.Model):
	entry_gw = models.ForeignKey(configdata, models.CASCADE, related_name="entry_GW")
	team_id = models.ForeignKey(CustomUser, models.CASCADE, related_name="entry_team")
	fixture_id1 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f1")
	score_home_fid1 = models.PositiveIntegerField(default=0)
	score_away_fid1 = models.PositiveIntegerField(default=0)
	fixture_id2 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f2")
	score_home_fid2 = models.PositiveIntegerField(default=0)
	score_away_fid2 = models.PositiveIntegerField(default=0)
	fixture_id3 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f3")
	score_home_fid3 = models.PositiveIntegerField(default=0)
	score_away_fid3 = models.PositiveIntegerField(default=0)
	fixture_id4 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f4")
	score_home_fid4 = models.PositiveIntegerField(default=0)
	score_away_fid4 = models.PositiveIntegerField(default=0)
	fixture_id5 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f5")
	score_home_fid5 = models.PositiveIntegerField(default=0)
	score_away_fid5 = models.PositiveIntegerField(default=0)
	fixture_id6 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f6")
	score_home_fid6 = models.PositiveIntegerField(default=0)
	score_away_fid6 = models.PositiveIntegerField(default=0)
	fixture_id7 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f7")
	score_home_fid7 = models.PositiveIntegerField(default=0)
	score_away_fid7 = models.PositiveIntegerField(default=0)
	fixture_id8 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f8")
	score_home_fid8 = models.PositiveIntegerField(default=0)
	score_away_fid8 = models.PositiveIntegerField(default=0)
	fixture_id9 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f9")
	score_home_fid9 = models.PositiveIntegerField(default=0)
	score_away_fid9 = models.PositiveIntegerField(default=0)
	fixture_id10 = models.ForeignKey(Fixtures, models.CASCADE, related_name="fid_f10")
	score_home_fid10 = models.PositiveIntegerField(default=0)
	score_away_fid10 = models.PositiveIntegerField(default=0)
	score_tg = models.PositiveIntegerField(default=0)
	scorer_player1 = models.ForeignKey('Players', on_delete=models.CASCADE, related_name="player1_scorer", null=True)
	scorer_player2 = models.ForeignKey('Players', on_delete=models.CASCADE, related_name="player2_scorer", null=True)
	scorer_player3 = models.ForeignKey('Players', on_delete=models.CASCADE, related_name="player3_scorer", null=True)
	scorer_player4 = models.ForeignKey('Players', on_delete=models.CASCADE, related_name="player4_scorer", null=True)

class Total_Goal_Entry(models.Model):
	entry_gw = models.ForeignKey(configdata, models.CASCADE, related_name="TG_Game_Week")
	team_id = models.ForeignKey(usr_teams, models.CASCADE, related_name="TG_Team")
	score_tg = models.PositiveIntegerField(default=0)

class entry_q_answers(models.Model):
	team_id = models.ForeignKey(usr_teams, models.CASCADE, related_name="qanwsers_team")
	entry_gw = models.ForeignKey(configdata, models.CASCADE, related_name="qanwsers_Game_Week")
	question_id = models.ForeignKey(Question, models.CASCADE, related_name="qanwsers_question_id")
	TRUE = 'TRUE'
	FALSE = 'FASLE'
	Q_CHOICES = [
        (TRUE, 'True'),
        (FALSE, 'False'),
    ]
	usr_answer = models.CharField(
        max_length=5,
        choices=Q_CHOICES,
        default=TRUE,
    )


class entry_scorers(models.Model):
	entry_gw = models.ForeignKey(configdata, models.CASCADE, related_name="scorers_gw_entry")
	team_id = models.ForeignKey(usr_teams, models.CASCADE, related_name="scorers_team_entry")
	entry_player1 = models.ForeignKey('Players', on_delete=models.CASCADE, default=0, related_name="player_score_1")
	entry_player2 = models.ForeignKey('Players', on_delete=models.CASCADE, default=0, related_name="player_score_2")
	entry_player3 = models.ForeignKey('Players', on_delete=models.CASCADE, default=0, related_name="player_score_3")
	entry_player4 = models.ForeignKey('Players', on_delete=models.CASCADE, default=0, related_name="player_score_4")



#needs work
class Results(models.Model):
	user = models.ForeignKey(configdata, models.CASCADE, related_name="Results_Team")
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
