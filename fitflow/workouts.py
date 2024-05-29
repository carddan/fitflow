from .models import Workout, CyclePhase, FitUser
#from .yoga_poses import get_yoga_poses
#from .constants import cycle_phase_mapping
from random import choice


def create_workouts():

    #menstrual_poses, shared_poses, luteal_poses = get_yoga_poses()
    CyclePhase.objects.get_or_create(name='Menstrual')
    CyclePhase.objects.get_or_create(name='Follicular')
    CyclePhase.objects.get_or_create(name='Ovulation')
    CyclePhase.objects.get_or_create(name='Luteal')

    menstrual_phase = CyclePhase.objects.get(name='Menstrual')
    follicular_phase = CyclePhase.objects.get(name='Follicular')
    ovulatory_day = CyclePhase.objects.get(name='Ovulation')
    luteal_phase = CyclePhase.objects.get(name='Luteal')

    workouts = []

    
    workout = Workout(
        name='Walking Meditation',
        description="""
        \t 1. Find a quiet outdoor space or walk on a treadmill indoors.\n
        \t 2. Begin walking at a slow, steady pace, focusing on the sensation\n 
        \t    of each step and the movement of your body.\n
        \t 3. Pay attention to your breath, inhaling deeply through the nose\n 
        \t    and exhaling fully through the mouth.\n
        \t 4. Notice the sights, sounds, and smells around you without judgment,\n 
        \t    simply observing the present moment.\n
        \t 5. Continue walking mindfully for 20-30 minutes, allowing yourself to\n 
        \t    feel grounded and connected to your surroundings.\n""",
        intensity='Low',
        duration='30 minutes',
        cycle_phase_id=menstrual_phase.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Gentle Yoga Flow',
        description="""
        \t  Indulge in a soothing and gentle yoga flow designed to nurture your\n 
        \t\tbody during the menstrual phase.\n\n
        \t 1. Begin in a comfortable seated position, focusing on deep, diaphragmatic \n
        \t    breathing to center yourself.\n
        \t 2. Move through gentle stretches and poses such as Cat-Cow, Child's Pose,\n 
        \t    and Supine Twist to alleviate menstrual discomfort and tension.\n
        \t 3. Embrace slow and mindful movements, listening to your body's cues and\n 
        \t    honoring any sensations that arise.\n
        \t 4. Incorporate restorative poses like Legs-Up-The-Wall and Supported Bridge Pose\n 
        \t    to promote relaxation and ease menstrual cramps.\n
        \t 5. Conclude with a brief Savasana (Corpse Pose), allowing yourself to fully\n 
        \t    surrender and rest deeply.\n\n
        \t  This gentle yoga flow will help calm your mind, soothe your body, and provide\n 
        \t\tmuch-needed relief during the menstrual phase.\n""",
        intensity='Low',
        duration='30 minutes',
        cycle_phase_id=menstrual_phase.id
    )
    workout.save()
    workouts.append(workout)


    workout = Workout(
        name='Restorative Pilates Flow',
        description="""
        \t  Rejuvenate your body and mind with a restorative Pilates flow designed to nurture\n 
        \t\tyour well-being during the menstrual phase.\n\n
        \t 1. Begin by lying on your back with knees bent and feet flat on the floor,\n 
        \t    focusing on deep breathing to center yourself.\n
        \t 2. Engage in gentle pelvic tilts and spine stretches to release tension\n 
        \t    in the lower back and hips.\n
        \t 3. Progress through a series of Pilates exercises such as leg circles,\n 
        \t    supine spine twists, and pelvic curls to strengthen the core and improve flexibility.\n
        \t 4. Embrace slow, controlled movements, honoring your body's needs and avoiding\n 
        \t    any strain or discomfort.\n
        \t 5. Incorporate props such as yoga blocks or pillows for added support and\n 
        \t    relaxation during stretches.\n
        \t 6. Conclude with a guided relaxation meditation, allowing yourself to fully\n 
        \t    surrender and find peace in the present moment.\n\n
        \t  This restorative Pilates flow will leave you feeling rejuvenated, balanced, and ready\n 
        \t\tto embrace the rest of your day with renewed energy.\n""",
        intensity='Low',
        duration='45 minutes',
        cycle_phase_id=menstrual_phase.id
    )
    workout.save()
    workouts.append(workout)


    workout = Workout(
        name='Light Cardio and Stretching Routine',
        description="""
        \t  Engage in a gentle and invigorating light cardio and stretching routine to\n 
        \t\tsupport your body during the menstrual phase.\n\n
        \t 1. Start with a brisk 10-minute walk or low-impact cardio activity such as\n 
        \t    cycling or swimming to increase blood flow and elevate your heart rate.\n
        \t 2. Follow up with dynamic stretches targeting major muscle groups, including arm circles,\n 
        \t    leg swings, and torso twists, to warm up your body and prepare for deeper stretches.\n
        \t 3. Move into a series of static stretches, holding each stretch for 20-30 seconds and\n 
        \t    focusing on deep breathing to enhance relaxation and flexibility.\n
        \t 4. Pay special attention to areas prone to tension and discomfort during menstruation,\n 
        \t    such as the lower back, hips, and abdomen, by incorporating stretches like seated\n 
        \t    forward folds, hip openers, and gentle twists.\n
        \t 5. Listen to your body's signals and adjust the intensity and duration of each stretch\n 
        \t    as needed to ensure comfort and safety.\n
        \t 6. Conclude with a brief cooldown period, allowing your heart rate to gradually return to\n 
        \t    normal and taking a moment to rest in a comfortable seated or lying position.\n\n
        \t  This light cardio and stretching routine will leave you feeling refreshed, rejuvenated,\n 
        \t\tand ready to embrace the day ahead with a sense of ease and vitality.\n""",
        intensity='Low',
        duration='30 minutes',
        cycle_phase_id=menstrual_phase.id
    )
    workout.save()
    workouts.append(workout)


    workout = Workout(
        name='Mindful Hiking Meditation',
        description="""
        \t  Immerse yourself in the beauty of nature and cultivate mindfulness with this serene\n 
        \t\thinking meditation, ideal for the luteal phase.\n\n
        \t 1. Choose a scenic hiking trail with varying terrain and levels of difficulty,\n 
        \t    ensuring it aligns with your fitness level and preferences.\n
        \t 2. Begin your hike with a mindful warm-up, focusing on your breath and setting\n 
        \t    an intention for your meditation practice.\n
        \t 3. As you walk, pay attention to the sensations in your body, the sights and\n 
        \t    sounds of the surrounding environment, and the rhythm of your footsteps.\n
        \t 4. Practice mindful walking by bringing your awareness to each step, feeling\n 
        \t    the connection between your feet and the earth beneath you.\n
        \t 5. Take moments to pause and appreciate the beauty around you, whether it's a\n 
        \t    breathtaking view, a serene waterfall, or a vibrant wildflower.\n
        \t 6. Engage your senses fully, noticing the scent of the forest, the feel of the\n 
        \t    breeze on your skin, and the sound of birdsong in the air.\n
        \t 7. Conclude your hike with a grounding meditation, finding a quiet spot to sit\n 
        \t    and center yourself in the present moment before heading back.\n\n
        \t  This mindful hiking meditation will leave you feeling refreshed, rejuvenated,\n 
        \t\tand deeply connected to the natural world around you.\n""",
        intensity='Low',
        duration='60 minutes',
        cycle_phase_id=luteal_phase.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Boxing Inspired Cardio Workout',
        description="""
        \t  Unleash your inner fighter and torch calories with this high-energy boxing inspired\n
        \t\tcardio workout, ideal for the luteal phase.\n\n
        \t 1. Start with a dynamic warm-up consisting of jumping rope, shadowboxing, and dynamic\n 
        \t    stretches to prepare your body for the intensity of the workout.\n
        \t 2. Move into a series of boxing-inspired exercises, including jabs, crosses, hooks,\n 
        \t    and uppercuts, performed on a punching bag or with shadowboxing.\n
        \t 3. Alternate between punching combinations and cardio intervals such as high knees,\n 
        \t    butt kicks, and jumping jacks to keep your heart rate elevated.\n
        \t 4. Focus on speed, power, and precision as you execute each punch, visualizing an\n 
        \t    opponent in front of you and giving it your all.\n
        \t 5. Take short breaks as needed to catch your breath and hydrate, but aim to maintain\n 
        \t    high level of intensity throughout the workout.\n
        \t 6. Conclude with a cooldown consisting of light shadowboxing, followed by static\n 
        \t    stretching to help your muscles recover and prevent soreness.\n
        \t  This boxing inspired cardio workout will leave you feeling strong, empowered, and\n 
        \t\tready to conquer the day with confidence and determination!\n""",
        intensity='High',
        duration='30 minutes',
        cycle_phase_id=luteal_phase.id
    )
    workout.save()
    workouts.append(workout)

    
    
    workout = Workout(
        name='Mood-Boosting Dance Cardio',
        description="""
        \t  Elevate your mood with this invigorating dance cardio workout, 
        \t\tperfect for the follicular phase.\n\n
        \t 1. Start with a dynamic warm-up, incorporating movements like shoulder rolls,\n 
        \t    hip circles, and gentle twists to loosen up your body and prepare for dance.\n
        \t 2. Follow along with energetic dance routines set to upbeat music, incorporating\n 
        \t    a variety of dance styles such as hip-hop, salsa, and jazz.\n
        \t 3. Embrace the freedom of movement, allowing yourself to let loose and express\n 
        \t    yourself fully through dance.\n
        \t 4. Focus on engaging your core muscles and maintaining good posture as you move\n 
        \t    to the rhythm, feeling the exhilaration of each step and movement.\n
        \t 5. Take breaks as needed to catch your breath and hydrate, but keep the energy\n 
        \t    high throughout the workout.\n
        \t 6. Conclude with a cool-down period, transitioning to slower, more fluid movements\n 
        \t    to gradually bring your heart rate down and promote relaxation.\n\n
        \t  This mood-boosting dance cardio session will leave you feeling energized, uplifted,\n 
        \t\tand ready to conquer the day with a smile!\n""",
        intensity='Moderate',
        duration='40 minutes',
        cycle_phase_id=follicular_phase.id
    )
    workout.save()
    workouts.append(workout)


    workout = Workout(
        name = 'Swimming',
        description = """
        \t  In a pool or the ocean, your choice. This is a simple, full body workout""",
        intensity = 'Moderate',
        duration = '30 minutes',
        cycle_phase_id=luteal_phase.id
    )
    workout.save()
    workouts.append(workout)
   

    workout = Workout(
        name = 'Biking',
        description = """
        \t Pedal your way to improved cardiovascular health, leg strength, and mental\n 
        \t\twell-being as you enjoy the ride.""",
        intensity = 'Moderate',
        duration = '45 minutes',
        cycle_phase_id=follicular_phase.id
    )
    workout.save()
    workouts.append(workout)


    workout = Workout(
        name = 'Stairmaster',
        description = """
        \t  Ready to feel the burn?\n 
        \t\tGet on a stairmaster and strengthen your quads, glutes, and core""",
        intensity = 'High',
        duration = '30 minutes',
        cycle_phase_id=ovulatory_day.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Interval Training Circuit',
        description="""
        \t  Ignite your metabolism and challenge your body with this high-intensity interval\n 
        \t\ttraining (HIIT) circuit, perfect for the ovulatory day.\n\n
        \t 1. Begin with a dynamic warm-up consisting of jumping jacks, high knees, and arm\n 
        \t    circles to elevate your heart rate and prepare your muscles for action.\n
        \t 2. Perform a series of bodyweight exercises, including burpees, mountain climbers,\n 
        \t    squat jumps, and push-ups, at maximum effort for 30 seconds each.\n
        \t 3. Rest for 20 seconds between exercises, allowing your heart rate to come down\n 
        \t    slightly before moving on to the next exercise.\n
        \t 4. Aim to complete 3-4 rounds of the circuit, pushing yourself to maintain intensity\n 
        \t    and effort throughout each round.\n
        \t 5. Focus on proper form and technique to maximize effectiveness and reduce the risk\n 
        \t    of injury.\n
        \t 6. Conclude with a cooldown consisting of light stretching and deep breathing to help\n 
        \t    your body recover and return to a resting state.\n\n
        \t  This interval training circuit will leave you feeling empowered, energized,
        \t\tand accomplished, ready to tackle whatever challenges come your way!\n""",
        intensity='High',
        duration='20 minutes',
        cycle_phase_id=ovulatory_day.id
    )
    workout.save()
    workouts.append(workout)


    workout = Workout(
        name = 'Inclined Walk',
        description = """
        \t  Get on a treadmill and set it at 12% incline 3mph.""",
        intensity = 'Moderate',
        duration = '30 minutes',
        cycle_phase_id=luteal_phase.id
    )
    workout.save()
    workouts.append(workout)
    
    workout = Workout(
        name="High-Intensity Interval Training (HIIT)",
        description="""
        \t 1. Warm up with 5 minutes of jump rope.\n
        \t 2. Perform a series of burpees, mountain climbers, and squat jumps, giving
        \t    maximum effort for 20-30 seconds.\n
        \t 3. Rest for 10-20 seconds between each exercise, allowing your heart rate to\n 
        \t    come down slightly before the next round.\n
        \t 4. Repeat the circuit 3-5 times, pushing yourself to maintain intensity throughout.\n
        \t 5. Cool down with 5 minutes of light stretching to help prevent muscle stiffness\n 
        \t    and aid in recovery.\n""",
        intensity="High",
        duration="25 minutes",
        cycle_phase_id=ovulatory_day.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Yin Yoga for Relaxation',
        description="""
        \t 1. Set up a comfortable yoga mat in a quiet, dimly lit space.\n
        \t 2. Begin with a seated meditation, focusing on deep, diaphragmatic breathing and\n 
        \t    cultivating a sense of inner calm.\n
        \t 3. Move into yin yoga poses such as butterfly pose, supported fish pose, and\n 
        \t    reclining twist, holding each pose for 3-5 minutes.\n
        \t 4. Focus on releasing tension and surrendering into each stretch, allowing\n 
        \t    gravity to gently open up the body.\n
        \t 5. Conclude with a brief Savasana (Corpse Pose) to integrate the benefits of your\n 
        \t    practice and promote deep relaxation.\n""",
        intensity='Low',
        duration='40 minutes',
        cycle_phase_id=luteal_phase.id
    )
    workout.save()
    workouts.append(workout)


    workout = Workout(
        name='Circuit Training',
        description="""
        \t 1. Set up a circuit with 5-6 different exercises targeting different muscle groups.\n
        \t 2. Perform each exercise for 45 seconds, followed by 15 seconds of rest or\n 
        \t    transition time.\n
        \t 3. Include a mix of bodyweight exercises, such as squats, lunges, push-ups,\n 
        \t    and planks, as well as cardio bursts like jumping jacks or high knees.\n
        \t 4. Complete 3-4 rounds of the circuit, aiming to maintain intensity and\n 
        \t    form throughout.\n
        \t 5. Cool down with 5-10 minutes of stretching to improve flexibility and\n 
        \t    prevent muscle soreness.\n""",
        intensity='Moderate',
        duration='30-45 minutes',
        cycle_phase_id=follicular_phase.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Guided Progressive Muscle Relaxation',
        description="""
        \t 1. Find a quiet and comfortable space to lie down on your back.\n
        \t 2. Begin by tensing the muscles in your feet, holding for a few seconds,\n 
        \t    and then releasing completely.\n
        \t 3. Move slowly up through your body, tensing and releasing each muscle\n 
        \t    group sequentially: calves, thighs, buttocks, abdomen, chest, arms,\n 
        \t    shoulders, neck, and face.\n
        \t 4. As you release each muscle group, focus on the sensation of relaxation and let go\n 
        \t    of any tension or stress.\n
        \t 5. Continue this process until you've relaxed all the muscles in your body,\n 
        \t    allowing yourself to sink\n 
        \t    into a state of deep relaxation.\n""",
        intensity='Low',
        duration='20 minutes',
        cycle_phase_id=luteal_phase.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Energizing Morning Yoga Flow',
        description="""
        \t 1. Start in a standing position at the top of your mat, feet hip-width apart,\n 
        \t    and arms by your sides.\n
        \t 2. Inhale, sweep your arms overhead, and exhale, forward fold, bending at the\n 
        \t    hips and reaching towards the ground.\n
        \t 3. Inhale, lift halfway, lengthening your spine, and exhale, fold forward again.\n
        \t 4. Step back into a high plank position, inhale, and exhale, lower\n 
        \t    down into a chaturanga.\n
        \t 5. Inhale, upward-facing dog, and exhale, downward-facing dog.\n
        \t 6. Hold downward-facing dog for a few breaths, then step or jump forward,\n 
        \t    returning to a forward fold.\n
        \t 7. Inhale, rise all the way up with arms overhead, and exhale, hands to heart center.\n
        \t 8. Repeat this flow for 5-10 rounds, focusing on linking breath with movement and\n 
        \t    building heat in the body.\n""",
        intensity='Moderate',
        duration='30 minutes',
        cycle_phase_id=follicular_phase.id
    )
    workout.save()
    workouts.append(workout)


    workout = Workout(
        name='Strength Training with Resistance Bands',
        description="""
        \t 1. Begin by securing a resistance band under your feet and holding the\n 
        \t    handles in each hand.\n
        \t 2. Start with bicep curls, keeping your elbows close to your sides and squeezing\n 
        \t    your biceps at the top of the movement.\n
        \t 3. Transition to shoulder presses, pressing the handles overhead while keeping\n
        \t    your core engaged and avoiding arching your back.\n
        \t 4. Move into squats, standing on the band with feet hip-width apart and holding\n 
        \t    the handles at shoulder height, then lowering into a squat position.\n
        \t 5. Finish with rows, stepping on the band with one foot, and pulling the handles\n 
        \t    towards your chest, squeezing your shoulder blades together.\n
        \t 6. Complete 3 sets of 12-15 repetitions for each exercise, focusing on maintaining\n 
        \t    proper form and controlled movements throughout.\n""",
        intensity='Moderate to High',
        duration='40 minutes',
        cycle_phase_id=ovulatory_day.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Dynamic Yoga Flow',
        description="""
        \t  Immerse yourself in a dynamic yoga flow practice that combines breath with movement
        \t\tto create a harmonious flow.\n
        \t 1. Perform the yoga poses Sun Salutations, Downward-Facing Dog, Warrior sequences,\n 
        \t    the Tree Pose, and finally the Eagle Pose.\n
        \t 2. Transition seamlessly from one posture to another, synchronizing breath and\n 
        \t    movement to enhance flexibility, strength, and mindfulness.\n\n
        \t  This invigorating practice will leave you feeling energized and centered, ready\n
        \t\tto take on the day with renewed vitality.\n""",
        intensity='Moderate',
        duration='60 minutes',
        cycle_phase_id=follicular_phase.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Total Body Strength',
        description="""
        \t  Embark on a comprehensive total body strength training session designed\n 
        \t\tto challenge and sculpt your muscles from head to toe.\n
        \t  Engage in the following exercises doing reps of 15 and sets until failure:\n\n

        \t - Barbell Squats: Load a barbell on your upper back, lower into a squat position\n 
        \t                   by bending your knees and hips, then return to standing. Targeting\n 
        \t                   the quadriceps, hamstrings, glutes, and lower back, barbell squats\n 
        \t                   build lower body strength and power.\n

        \t - Romanian Deadlifts: Hold a barbell in front of your thighs with an overhand grip,\n 
        \t                       hinge at your hips to lower the barbell towards the ground,\n 
        \t                       then return to standing by contracting your hamstrings and glutes.\n 
        \t                       Romanian deadlifts strengthen the posterior chain and improve\n 
        \t                       overall stability.\n

        \t - Bent-Over Rows: Hold a barbell with an overhand grip, hinge at your hips to lower your\n 
        \t                   torso towards the ground, then pull the barbell towards your\n
        \t                   lower chest, squeezing your shoulder blades together. Bent-over rows\n 
        \t                   develop a strong and balanced upper back, shoulders, and arms.\n

        \t - Dumbbell Shoulder Presses: Hold a pair of dumbbells at shoulder height, palms facing\n 
        \t                              forward, then press the weights overhead until your arms\n 
        \t                              are fully extended. Lower the dumbbells back to shoulder height\n 
        \t                              and repeat. Dumbbell shoulder presses strengthen the deltoids,\n 
        \t                              triceps, and stabilizer muscles.\n\n

        \t  Incorporating these specific exercises allows for targeted muscle engagement and\n 
        \t\tprogressive overload, promoting muscle growth, strength, and endurance. With each\n 
        \t\trepetition, feel yourself growing stronger and more resilient, ready to conquer any\n 
        \t\tchallenge that comes your way.\n""",
        intensity='High',
        duration='45 minutes',
        cycle_phase_id=ovulatory_day.id
    )
    workout.save()
    workouts.append(workout)


    workout = Workout(
        name='Core Crusher',
        description="""
        \t  Sculpt your core with this intense core-strengthening workout.\n
        \t 1. Start with a dynamic warm-up: Perform light jogging in place, arm circles,\n 
        \t    and leg swings to increase blood flow and loosen up your muscles.\n
        \t 2. Dive into targeted exercises:
        \t      a. Crunches: Lie on your back with knees bent, hands behind your head,\n 
        \t         and lift your shoulders off the ground.
        \t      b. Russian twists: Sit on the floor, lean back slightly, and rotate your torso\n 
        \t         from side to side while holding a weight or keeping your hands clasped together.\n
        \t      c. Bicycle crunches: Lie on your back, lift your legs off the ground, and bring\n 
        \t         opposite elbow to knee in a cycling motion.\n
        \t      d. Leg raises: Lie on your back, keep your legs straight, and lift them towards the\n 
        \t         ceiling, then lower them back down without touching the floor.\n
        \t      e. Plank variations: Hold a plank position on your forearms or hands, engaging your\n 
        \t         core and keeping your body in a straight line from head to heels.\n
        \t 3. Focus on proper form and controlled movements throughout each exercise.\n
        \t 4. Progress through 3-4 sets of 8-12 repetitions for each exercise, taking short breaks\n 
        \t    between sets to catch your breath.\n
        \t 5. Feel the burn intensify with each repetition, pushing through the discomfort to\n 
        \t    strengthen your core muscles from every angle.\n
        \t 6. Conclude with a soothing cooldown: Perform gentle stretches like cat-cow, child's pose,\n 
        \t    and spinal twists to release tension and promote recovery.\n""",
        intensity='Moderate',
        duration='30 minutes',
        cycle_phase_id=luteal_phase.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Cardio Kickboxing',
        description="""
        \t  Step into the ring with this exhilarating cardio kickboxing workout.\n
        \t 1. Begin with a dynamic warm-up:\n
        \t      a. Jumping jacks: Start with your feet together, then jump and spread your legs\n 
        \t         while raising your arms overhead.\n
        \t      b. Arm circles: Stand tall and rotate your arms in small circles, gradually increasing\n 
        \t         the size of the circles.\n
        \t      c. Leg swings: Hold onto a stable surface and swing one leg forward and backward, then\n 
        \t         side to side, to loosen up your hips and legs.\n
        \t 2. Learn or perform basic kickboxing techniques:\n
        \t      a. Jabs: Extend your lead hand straight out in front of you, keeping your other hand\n 
        \t         close to your face for protection.\n
        \t      b. Crosses: Rotate your back hip and shoulder forward while extending your rear hand\n 
        \t         straight out in front of you.\n
        \t      c. Hooks: Bend your arm at a 90-degree angle and swing it horizontally across your\n 
        \t         body, aiming to strike with the side of your fist.\n
        \t      d. Front kicks: Lift your knee, extend your leg forward, and then snap it back quickly to\n 
        \t         kick with the ball of your foot.\n
        \t 3. String together dynamic combinations: Practice combining the techniques you've learned into\n 
        \t    fluid, continuous movements.\n
        \t 4. Feel the adrenaline surge as you punch, kick, and move to the beat of energizing music,\n 
        \t    releasing stress and tension with every strike.\n
        \t 5. Push yourself to the limit and leave it all on the mat as you sweat your way through this\n 
        \t    high-energy workout.\n
        \t 6. Cool down with calming stretches and deep breaths to bring your heart rate down and\n 
        \t    promote recovery!!""",
        intensity='High',
        duration='45 minutes',
        cycle_phase_id=ovulatory_day.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
    name='Strength and Stretch Yoga Fusion',
    description="""
    \t  Experience the perfect balance of strength-building and flexibility-enhancing yoga poses\n 
    \t\twith this fusion workout, ideal for the ovulatory day.\n
    \t 1. Begin with a grounding meditation, focusing on your breath and setting an intention\n 
    \t    for your practice.\n
    \t 2. Warm up your body with Sun Salutations, flowing through each pose with fluid movements\n 
    \t    and deep breaths.
    \t 3. Move into a series of strength-building yoga poses such as Warrior II, Chair Pose, and Plank,\n 
    \t    holding each pose for several breaths to build endurance and stability.\n
    \t 4. Transition into deep stretches targeting major muscle groups, including hips, hamstrings, and\n 
    \t    shoulders, to release tension and improve flexibility.\n
    \t 5. Focus on maintaining proper alignment and engaging your core throughout the practice to\n 
    \t    maximize the benefits of each pose.\n
    \t 6. Conclude with a calming Savasana, allowing yourself to fully relax and integrate the physical\n 
    \t    and mental benefits of your practice.\n\n
    \t  This Strength and Stretch Yoga Fusion will leave you feeling strong, flexible, and centered as you\n 
    \t\tmove through your ovulatory day with grace and ease.""",
    intensity='Moderate',
    duration='60 minutes',
    cycle_phase_id=ovulatory_day.id
    )
    workout.save()
    workouts.append(workout)
    
    
    workout = Workout(
        name='Strength and Stability Circuit',
        description="""
        \t  Build strength and enhance stability with this circuit-style workout.\n
        \t 1. Start with a dynamic warm-up consisting of jogging in place, arm circles, and leg swings\n 
        \t    to prepare your body for movement.\n
        \t 2. Perform 15 reps of 3 sets of these strength exercises targeting major muscle groups: squats,\n 
        \t    lunges, push-ups, and rows, using dumbbells or resistance bands.\n
        \t 3. Focus on maintaining proper form and engaging your core throughout each exercise to maximize\n 
        \t    effectiveness and minimize the risk of injury.\n
        \t 4. Also incorporate some of these stability exercises of 15 reps of 3 sets: plank variations,\n 
        stability ball crunches, and single-leg balance exercises, to challenge your balance and core stability.\n
        \t 5. Progress through the circuit, alternating between strength and stability exercises.\n
        \t 6. Conclude with a cooldown consisting of gentle stretches for the major muscle groups worked\n
        \t    during the workout.
        """,
        intensity='High',
        duration='45 minutes',
        cycle_phase_id=ovulatory_day.id
    )
    workout.save()
    workouts.append(workout)

    
    return workouts

