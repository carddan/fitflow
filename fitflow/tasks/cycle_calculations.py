from ..models import FitUser, Workout, CyclePhase
from datetime import datetime
from ..workouts import create_workouts
import pickle
import json
import random



def get_days_since_last_period(last_period):
    today = datetime.now().date()
    days_since_last_period = (today - last_period).days
    return days_since_last_period

#using default values for new users since not enough info to use model yet
def get_new_user_cycle_length(user):
    age_range=user.age_range
    if age_range in ('1'):
        cycle_length = 30
    elif age_range in ('2', '3'):
        cycle_length = 29
    else: 
        cycle_length = 28

    return cycle_length

#using the trained model to calculate lengths 
def predict_future_lengths(user):
    #load the trained model
    with open ('C:/Users/daniella/DC/cycle_analysis/model.pkl', 'rb') as f:
        model = pickle.load(f)
    #prepare input data for prediction
    input_data = [[user.previous_cycle_lengths, user.previous_luteal_lengths]]

    predicted_lengths = model.predict(input_data)
    predicted_cycle_length = predicted_lengths[0]
    predicted_luteal_length = predicted_lengths[1]
    return predicted_cycle_length, predicted_luteal_length


def get_cycle_and_luteal_length(user):
    previous_cycle_lengths = json.loads(user.previous_cycle_lengths)
    if len(previous_cycle_lengths) >=3:
        predicted_cycle_length = user.predicted_cycle_length 
        predicted_luteal_length = user.predicted_luteal_length
        cycle_length, luteal_length = predicted_cycle_length, predicted_luteal_length
      
    else:
        cycle_length = get_new_user_cycle_length(user)
        luteal_length = 13
        print('this one is working')

    user.cycle_length = cycle_length
    user.luteal_length = luteal_length
    user.save()
    return cycle_length, luteal_length

def get_period_length(user):
    age_range = user.age_range
    previous_period_lengths = json.loads(user.previous_period_lengths)
    previous_cycle_lengths = json.loads(user.previous_cycle_lengths)
    if len(previous_cycle_lengths) >=3:
        period_length = sum(previous_period_lengths) / len(previous_period_lengths)
    else:
        if age_range in ('1'):
            period_length = 6
        elif age_range in ('2', '3'):
            period_length = 5
        else:
            period_length = 4
    
    user.period_length = period_length
    user.save()
    return period_length
    

#follicular is length of period, fertility_window_start, ovulation, and more 
#therefore, follicular length is cycle length minus luteal length and fertility_window_end length which is 1
#-2 so that ovulatory day can be it's own section of 'Ovulation'
def get_follicular_length(user):
    follicular_length = user.cycle_length - user.luteal_length - 1
    print('follicular_length')
    print(follicular_length)
    user.follicular_length = follicular_length
    user.save()
    print(user.follicular_length)
    return follicular_length

def get_ovulatory_day(user):
    ovulatory_day = user.follicular_length
    print('ovulatory day')
    print(ovulatory_day)
    user.ovulatory_day = ovulatory_day
    user.save()
    print(user.ovulatory_day)
    return ovulatory_day


def get_fertility_window(user):
    #calculate window as 4 days before and 1 after ovulation 
    fertility_window_start = user.ovulatory_day -4
    fertility_window_end = user.ovulatory_day + 1

    #ensure the window doesn't exceed cycle length
    fertility_window_start = max(1, fertility_window_start)
    fertility_window_end = min(user.cycle_length, fertility_window_end)
    user.fertility_window_start = fertility_window_start
    user.fertility_window_end = fertility_window_end
    user.save()
    return range(fertility_window_start +1, fertility_window_end)


def get_cycle_phase(user):
    days_since_last_period = get_days_since_last_period(user.last_period)
    

    if days_since_last_period <= user.period_length:
        cycle_phase = 'Menstrual'
    elif days_since_last_period < user.follicular_length:
        cycle_phase = 'Follicular'
    elif days_since_last_period <= user.ovulatory_day:
        cycle_phase = 'Ovulation'
    else:
        cycle_phase = 'Luteal'
    cycle_phase, created = CyclePhase.objects.get_or_create(name= cycle_phase)
    user.cycle_phase = cycle_phase
    return cycle_phase


def get_filtered_workouts(user):
    print(user.cycle_phase)
    # Filter workouts based on the user's cycle phase
    filtered_workouts = Workout.objects.filter(cycle_phase__exact=user.cycle_phase)

    # Get the count of filtered workouts
    count = filtered_workouts.count()

    # If there are less than 3 workouts available, return all of them
    if count <= 3:
        return filtered_workouts

    # Otherwise, select 3 random workouts
    random_workouts = random.sample(list(filtered_workouts), 3)
    
    return random_workouts









