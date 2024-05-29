from django.db import models
from django.conf import settings
import datetime
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
import pickle
import json

with open('C:/Users/daniella/DC/cycle_analysis/model.pkl', 'rb') as f:
    model = pickle.load(f)

class CyclePhase(models.Model):
    name = models.CharField(max_length=25, choices=(
        ('Menstrual', 'Menstrual'),
        ('Follicular', 'Follicular'),
        ('Ovulation', 'Ovulation'),
        ('Luteal', 'Luteal'),
    ))
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class FitUser(AbstractUser, PermissionsMixin):

    def normalize_email(self, email):
        return email.lower().strip()

    def get_username(self):
        return self.username.lower()

    username = models.CharField(max_length=100, unique=True, blank=False, default= "default_user")
    firstname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)   
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    AGE_RANGE_CHOICES = [
        ('1', 'Under 18'),
        ('2', '18-29'),
        ('3', '30-39'),
        ('4', '40-49'),
        ('5', '50+'),
    ]

    age_range = models.CharField(max_length=20, choices=AGE_RANGE_CHOICES)
    last_period = models.DateField( blank=True)
    EXERCISE_PURPOSE_CHOICES = [
        ('loseWeight', 'Lose Weight'),
        ('buildMuscle', 'Build Muscle'),
        ('stayActive', 'Stay Active'),
    ]
    exercise_purpose = models.CharField(max_length=20, choices=EXERCISE_PURPOSE_CHOICES)
    #pickled_model = models.pickled_model.PickledModelField(default=model)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    activation_link_sent_at = models.DateTimeField(null=True, blank=True)


    #FIELDS RELATED TO MENSTRUAL CYCLE

    previous_cycle_lengths = models.TextField(default='[]')
    previous_luteal_lengths = models.TextField(default='[]')
    predicted_cycle_length = models.PositiveIntegerField(null=True, blank=True)
    predicted_luteal_length = models.PositiveIntegerField(null=True, blank=True)
    cycle_length = models.PositiveIntegerField(null=True, blank=True)
    luteal_length = models.PositiveIntegerField(null=True, blank=True)
    cycle_phase = models.ForeignKey(CyclePhase, on_delete=models.SET_NULL, null=True, blank=True)

    #method to add new cycle lengths
    def add_cycle_length(self, cycle_length):
        cycle_lengths = json.loads(self.previous_cycle_lengths)
        cycle_lengths.append(cycle_length)
        if len(cycle_lengths) > 3:
            cycle_lengths.pop(0)
        self.previous_cycle_lengths = json.dumps(cycle_lengths)
        self.save()

    #method to add new luteal phase length 
    def add_luteal_length(self, luteal_length):
        luteal_lengths = json.loads(self.previous_luteal_lengths)
        luteal_lengths.append(luteal_length)
        if len(luteal_lengths) > 3:
            luteal_lengths.pop(0)
        self.previous_luteal_lengths = json.dumps(luteal_lengths)
        self.save()


    follicular_length = models.PositiveIntegerField(null=True, blank=True)
    ovulatory_day= models.PositiveIntegerField(null=True, blank=True)
    fertility_window_start = models.PositiveIntegerField(null=True, blank=True)
    fertility_window_end = models.PositiveIntegerField(null=True, blank=True)
    
    #List to store previous period lengths
    period_length = models.PositiveIntegerField(null=True, blank=True)
    previous_period_lengths = models.TextField(default='[]')

    #method to add new period lengths
    def add_period_length(self, period_length):
        previous_periods = json.loads(self.previous_period_lengths)
        previous_periods.append(period_length)
        self.previous_period_lengths = json.dumps(previous_periods)
        self.save()
    
        

    class Meta:
        verbose_name = 'Fit User'
        verbose_name_plural = 'Fit Users'

    
    def __str__(self):
        return self.firstname


class FitUserManager(BaseUserManager):

    def create_user(self, username, email, password, firstname, last_period, age_range, exercise_purpose):
        email = self.normalize_email(email)
        user = FitUser.objects.create_user(username=username, email=email, firstname= firstname, last_period=last_period, 
                          age_range=age_range, exercise_purpose= exercise_purpose)
        user.set_password(password)
        user.save()
        return user
   


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    intensity = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    cycle_phase = models.ForeignKey('CyclePhase', on_delete=models.CASCADE)
    #for_goals = models.IntegerField()
    def __str__(self):
        return self.name
    


class MenstrualPhase(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    def __str__(self):
        return self.name
    

    




