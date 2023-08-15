from .cycle_calculations import get_cycle_and_luteal_length, get_period_length, get_ovulatory_day, get_fertility_window, get_follicular_length
from .cycle_calculations import get_cycle_phase, get_filtered_workouts
from datetime import date, timedelta, datetime
from ..models import FitUser, CyclePhase
from celery import shared_task
from django.core.cache import cache
#from ..workouts import create_workouts
#from ..constants import cycle_phase_mapping 


#for new users and returning users
def new_cycle_data(user):
    cycle_length, luteal_length = get_cycle_and_luteal_length(user)
    period_length = get_period_length(user)
    follicular_length = get_follicular_length(user)
    ovulatory_day = get_ovulatory_day(user)
    fertility_window = get_fertility_window(user)
    cycle_phase = get_cycle_phase(user)

    # Initialize user's model with the calculated values
    user.cycle_length = cycle_length
    user.luteal_length = luteal_length
    user.period_length = period_length
    user.follicular_length = follicular_length
    user.ovulatory_day = ovulatory_day
    user.fertility_window = fertility_window
    user.cycle_phase = cycle_phase

    user.save()

    return cycle_length, luteal_length, period_length, ovulatory_day, follicular_length, cycle_phase


#function to be called when cycle done
def end_of_cycle_processing(user):

    cycle_length, luteal_length, period_length, ovulatory_day, follicular_length, cycle_phase = new_cycle_data(user)

    return cycle_length, luteal_length, period_length, ovulatory_day, follicular_length, cycle_phase

#can be used to make sure that the cycle has not yet ended for returning users and continuous users?
#for continous users maybe we should have a function that is for the length of the cycle, and within that code the day of cycle phase is generated?
def user_cycle_has_ended(user):
    days_since_last_period = (date.today() - user.last_period).days
    return days_since_last_period >= user.cycle_length

#this is to update the last period date for returning users
def update_last_period_for_returning_users(user):
    last_cycle_length = user.cycle_length
    first_day_of_new_cycle = datetime.now().date() - timedelta(days = last_cycle_length)
    user.last_period = first_day_of_new_cycle
    user.save()


@shared_task
def up_to_date(user_id):
    user = FitUser.objects.get(id=user_id)

    #checks if the user's cycle has ended
    if user_cycle_has_ended(user):
        user.add_cycle_length(user.cycle_length)
        user.add_luteal_length(user.luteal_length)
        user.add_period_length(user.period_length)
        new_cycle_data(user)
        #update last_period variable
        user.last_period = datetime.now().date() 
        user.save()
        #get user's cycle phase
        cycle_phase = [user.cycle_phase]
        fitness_goals = user.exercise_purpose.all()
        #create_workouts()
        recommended_workouts = get_filtered_workouts(user, cycle_phase, for_goals=fitness_goals)
        user.save()
    else:
        cycle_phase = [user.cycle_phase]
        #get user's recommended workouts
        fitness_goals = user.exercise_purpose.all()
        #create_workouts()
        recommended_workouts = get_filtered_workouts(user, cycle_phase, for_goals=fitness_goals)
        user.save()
    
    return cycle_phase, recommended_workouts
#note this returns a tuple, so to separate you can do tuple unpacking 
        
#cache the up_to_date function's results every day at midnight
def cache_up_to_date_results(user_id):
    user = FitUser.objects.get(id=user_id)
    #create_workouts()
    cycle_phase, recommended_workouts = up_to_date(user_id)

    #Cache the results w/ an expiration time until the next day
    now = datetime.now()
    next_midnight = datetime.combine(now.date() + timedelta(days=1), datetime.min.tim())
    cache_timeout = (next_midnight - now).seconds
    cache.set('up_to_date_menstrual_phase', cycle_phase, timeout=timedelta(days=1))
    cache.set('up_to_date_recommended_workouts', recommended_workouts, timeout=timedelta(days=1))


#so that mainpg doesn't perform up_to_date on new users
def is_first_time_user(user):
    current_time = datetime.now()
    creation_time = user.date_joined 
    time_since_creation = current_time - creation_time
    return time_since_creation <=timedelta(days=1)




