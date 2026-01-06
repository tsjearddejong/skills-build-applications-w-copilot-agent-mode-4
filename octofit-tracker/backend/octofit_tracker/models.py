from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    class Meta:
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        db_table = 'activities'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        db_table = 'workouts'
