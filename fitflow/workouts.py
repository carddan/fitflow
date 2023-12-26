from .models import Workout, CyclePhase, FitUser
#from .yoga_poses import get_yoga_poses
#from .constants import cycle_phase_mapping


def create_workouts():
    #menstrual_poses, shared_poses, luteal_poses = get_yoga_poses()
    menstrual_phase = CyclePhase.objects.get(name='Menstrual')
    follicular_phase = CyclePhase.objects.get(name='Follicular')
    ovulatory_day = CyclePhase.objects.get(name='Ovulation')
    luteal_phase = CyclePhase.objects.get(name='Luteal')

    
    workouts = []

    '''
    workout = Workout(
        name = "Beginner's Yoga",
        description ='This is a low intensity workout suitable for even your heaviest of flow days!',
        intensity ='Moderate',
        duration = '25 minutes',
        yoga_poses = [
            menstrual_poses["Child's Pose"],
            menstrual_poses["Cat-cow Pose"],
            menstrual_poses["Downward-Facing Dog Pose"],
        ]
    )
    workout.save() #save the workout instance first
    workout.cycle_phase.set([menstrual_phase])
    workout.for_goals.set([lose_weight_goal.id, build_muscle_goal.id, stay_active_goal.id])
    workouts.append(workout)

    workout = Workout(
        name="Beginner's Yoga!",
        description = 'As your energy continues to wane, these yoga poses can  ',
        intensity = 'Moderate',
        duration = '25 minutes',
        yoga_poses=[
            luteal_poses['Four-Limbed Staff Pose'],
            luteal_poses['Boat Pose'],
            shared_poses['Triangle Pose'],
            shared_poses['Warrior II Pose']
        ]
    )
    workout.save()
    workout.cycle_phase.set([luteal_phase])
    workout.for_goals.set([lose_weight_goal.id, build_muscle_goal.id])
    workouts.append(workout)

    '''
    
    workout = Workout(
        name = 'Mindfullness Walk',
        description = "Your energy is at a low. Go on a walk and focus on your breathing and happy thoughts.",
        intensity = "Low",
        duration = "45 minutes",
        cycle_phase_id=menstrual_phase.id
    )
    workout.save()



    workout = Workout(
        name = 'Swimming',
        description = 'In a pool or the ocean, your choice. This is a simple, full body workout ',
        intensity = 'Moderate',
        duration = '30 minutes',
        cycle_phase_id=luteal_phase.id
    )
    workout.save()
   

    workout = Workout(
        name = 'Biking',
        description = 'Be like Frank Ocean and go for a bike ride. ',
        intensity = 'Moderate',
        duration = '45 minutes',
        cycle_phase_id=follicular_phase.id
    )
    workout.save()


    workout = Workout(
        name = 'Stairmaster',
        description = 'Ready to feel the burn? Get on that stairmaster and strengthn your quads, glutes, and core',
        intensity = 'High',
        duration = '30 minutes',
        cycle_phase_id=ovulatory_day.id
    )
    workout.save()
    workout.cycle_phase.set([follicular_phase, ovulatory_day])
    workouts.append(workout)

    workout = Workout(
        name = 'Inclined Walk',
        description = 'Get on a treadmill and set it at 12% incline 3mph. ',
        intensity = 'Moderate',
        duration = '30 minutes',
        cycle_phase_id=luteal_phase.id
    )
    workout.save()

    

    print(workouts)
    return 


workouts=Workout.objects.all()
print('passing workouts.py')
print(workouts)
    
    