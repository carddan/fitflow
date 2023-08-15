'''
def get_yoga_poses():
    #remember that yoga_poses dictionary is for 
    menstrual_poses = {
        "Child's Pose" : {
            "name" : "Child's Pose",
            "description" : "This exercise helps relax the spine and hips.",
            "steps" : """1. Kneel on the floor with your knees hip-width apart and your hands in front of your shoulders.\n2. As you exhale, 
            bring your torso down to your thighs and rest your forehead on the floor. Rest your arms alongside your thighs with palms facing up\n3. Relax
            your muscles and take several slow breaths.""",
            "intensity" : "Low"
        },
        "Cat-cow Pose" : {
            "name" : "Cat-cow Pose",
            "description" : "This is a great way to stretch the spine.",
            "steps" : """1. Start on your hands and knees.\n2. As you inhale, curve your back like a cat.\n3. As you exhale, round your back like a cow, 
            pelvis up.\n4. Repeat this several times.""",
            "intensity" : "Low"
        },
        "Downward-facing Dog Pose" : {
            "name" : "Downward-facing Dog Pose",
            "description" : "This exercise helps stretch the hamstrings and calves.",
            "steps" : """1. Start on your hands and knees with your hands shoulder-distance apart.\n2. As you inhale, lift your hips up towards the ceiling.\n3.  
            Exhale as you straighten your legs until your heels touch the ground.\n4. Make sure that your shoulders are lifted away from the ears and palms are 
            flat on the floor.\n5. Your body should form an upside-down V shape, keep inhaling and exhaling evenly as you hold the pose for several breaths.""",
            "intensity" : "Low"
        }
    }

    shared_poses = {
        "Warrior II Pose" : {
            "name" : "Warrior II Pose",
            "description" : "This is a great way to build strength and balance.",
            "steps" : """1. Start in a lunge position with your arms resting to your sides.\n2. Move your back leg further back until straightened. Make sure your 
            foot is flat on the floor and at a 45 degree angle.\n3. Instead of facing straight ahead, face the side like your torso.\n4. Bring your arms parallel to 
            the ground, and reach your front arm towards the front and back arm towards the back\n5. Hold this position for several more breaths and focus on your breathing. """,
            "intensity" : "Moderate"
        },
        "Triangle Pose" : {
            "name" : "Triangle Pose",
            "description" : "This exercise helps strengthen and increase mobility of the hips, shoulders, hamstrings, and calves. ",
            "steps" : """1. Start in a standing position with your feet hip-width apart.\n2. Bend your right knee and place your right foot on the floor 
            in front of you.\n3. Rotate your torso to the right so that your right arm is parallel to the ground and your left arm is reaching up toward the sky.\n4. Hold
            this position for several more breaths. """,
            "intensity": "Moderate"
        }

    }

    luteal_poses = {
        "Four-Limbed Staff Pose" : {
            "name" : "Four-Limbed Staff Pose",
            "description" : "This exercise helps strengthn your core and upper body muscles.",
            "steps" : """1. Start on your hands and knees hip-width apart.\n2. As you inhale lift knees and straighten legs, distributing your weight evenly between 
             hands and toes.\n3. As you exhale bend your elbows straight back, not to the sides, as you lower your body into a straight line until it's only a 
             few inches off the ground.\n4. Repeat this several more time. """,
             "intensity" : "High"
        },
        "Boat Pose" : {
            "name" : "Boat Pose",
            "description" : "This pose helps strengthen your core and legs.",
            "steps" : """1. Start by sitting on the floor with your legs straight out in front of you. Lean back a bit and lift your feet off the floor, balancing
             on your butt.\n2. Lift your arms straight in front of you, keeping them parallel to the floor.\n3. Hold this posiiton for 5 to 10 breaths, focusing on
              your breath and maintaining balance. """,
              "intensity" : "High"
        }
        
        

    }

    return menstrual_poses, shared_poses, luteal_poses

'''
