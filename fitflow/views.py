from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import FitUser, FitUserManager, Workout, CyclePhase
from django.contrib.auth import authenticate, logout,login, get_user_model
from datetime import date, datetime, timedelta
from django.conf import settings
from django.utils.datastructures import MultiValueDictKeyError
from django.forms import ModelForm
from .tasks.cycle_calculations import get_filtered_workouts, get_cycle_phase 
from .tasks.cycle_processing import new_cycle_data, end_of_cycle_processing, user_cycle_has_ended, update_last_period_for_returning_users
from .tasks.cycle_processing import up_to_date, is_first_time_user
from django.core.cache import cache
from .workouts import create_workouts
from .constants import EXERCISE_PURPOSE_MAPPING

# Create your views here.
def app(request):
    return render(request, 'app.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password1 = request.POST["password1"]
        user= authenticate(request, email=email, password=password1)
        if user is not None:
            login(request, user)
            if user_cycle_has_ended(user):
                update_last_period_for_returning_users(user)
                user.add_cycle_length(user.cycle_length)
                user.add_luteal_length(user.luteal_length)
                user.add_period_length(user.period_length)
                end_of_cycle_processing(user)
            return redirect('mainpg')
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'login.html')
        
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
        except MultiValueDictKeyError as e:
            messages.error(request, 'Please enter a username.')
            return redirect('signup')

        firstname = request.POST['firstname']
        email = request.POST['email']
        age_range = request.POST['ageRange']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        exercise_purpose = request.POST['exercisePurpose']
        #had to do the following bc of an error
        date_string = request.POST['lastPeriod']
        try:
            last_period = datetime.strptime(date_string, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, 'Invalid date format')
            return render(request, 'signup.html')

        
        print("Sign up form submitted")

        if password1!= password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')
        
        if FitUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request,'signup.html')
        
        if FitUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request,'signup.html')
        
        user = FitUser.objects.create_user(username=username, email=email, password=password1, 
                                          firstname=firstname, last_period=last_period, 
                                          age_range=age_range, exercise_purpose=exercise_purpose)
        user.save()

        #initialize cycle data for the new user
        new_cycle_data(user)

        
        print("User information stored:")
        print(f"Username: {user.username}")
        print(f"Name: {user.firstname}")
        print(f"Email: {user.email}")
        print(f"Password: {user.password}")
        print(f"Age Range: {user.age_range}")
        print(f"Last Period: {user.last_period}")
        print(f"Exercise Purpose: {user.exercise_purpose}")

        return redirect('login')
    
    return render(request, 'signup.html')

def forgotp (request):
    return render(request, 'forgotp.html')

def logout(request):
    logout(request)
    return redirect('app')


def mainpg(request):
    user=request.user
    cached_results = cache.get(f'up_to_date_results_{user.id}')

    if cached_results is None and not is_first_time_user:
        cycle_phase, recommended_workouts = up_to_date(user.id)
        print('not cached!')
        cache.set(f'up_to_date_results_{user.id}', (cycle_phase, recommended_workouts), timeout=None)
    elif not is_first_time_user:
        cycle_phase, recommended_workouts = cached_results
    else: 
        cycle_phase=user.cycle_phase
        recommended_workouts = get_filtered_workouts(user)
        print('recommended workouts', recommended_workouts)
        print(recommended_workouts.values())

    return render(request, 'mainpg.html', {
        'cycle_phase': cycle_phase,
        'recommended_workouts' : recommended_workouts
    })
        
    






