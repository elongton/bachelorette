import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bachelorette.settings')

import django
django.setup()
from django.core.management import execute_from_command_line


from django.contrib.auth.models import User
from questions.models import Place

execute_from_command_line(['manage.py', 'migrate'])
input("Press Enter to continue...")

place_array = [None] * 7
place_array[0] = {'place_id': 1,
                 'next_id': 2,
                 'instructions': "All that foot stuff gave you an appetite! Order whatever you like, alcoholic beverages included.  It's on me :)",
                 'plank_clue': 'Find the next plank within Mellow Mushroom.  Here\'s your clue: Hindenburg',
                 'plank_prompt': 'Answer the plank for the next clue:',
                 'name_of_establishment': 'Mellow Mushroom',
                 'plank_answer': 'Lee Jordan',
                 'is_current': True,
                 'location_complete': False}
place_array[1] = {'place_id': 2,
                 'next_id': 3,
                 'instructions': 'Okay, walk over to 3100 Ellwood Avenue.  Don\'t worry, it\'s only 0.1 miles.',
                 'plank_clue': 'Find the next plank within Belmont Library.  Here\'s your clue: Where could one read about a "Kneazle"?',
                 'plank_prompt': 'Once you have the plank, answer this for your next location: Which game is this from?',
                 'name_of_establishment': 'Belmont Library',
                 'plank_answer': 'Final Fantasy X',
                 'is_current': False,
                 'location_complete': False}
place_array[2] = {'place_id': 3,
                 'next_id': 4,
                 'instructions': 'Next address is 2930 W Cary St. About 0.2 miles this time. Also, make sure you say hi to "MJ" for me!  Perhaps send a group photo?',
                 'plank_clue': 'Find the next plank within Bits and Pixels.  Here\'s your clue: Biggs & Wedge have important info for AVALANCHE.',
                 'plank_prompt': 'Answer the plank for your next location:',
                 'name_of_establishment': 'Bits and Pixels',
                 'plank_answer': 'Five',
                 'is_current': False,
                 'location_complete': False}
place_array[3] = {'place_id': 4,
                 'next_id': 5,
                 'instructions': 'Next address is 3111 W Cary St.  I think it\'s about time for a drink, wouldn\'t you say?  I recommend the Busky RVA cider, and have a cupcake if you like.',
                 'plank_clue': 'Find the next plank within Carytown Cupcakes.  Here\'s your clue:  Coconut Creamer',
                 'plank_prompt': 'Once you have the plank, answer this for your next location:  Song this line is from:',
                 'name_of_establishment': 'Carytown Cupcakes',
                 'plank_answer': 'Be Prepared',
                 'is_current': False,
                 'location_complete': False}
place_array[4] = {'place_id': 5,
                 'next_id': 6,
                 'instructions': 'Next address is 3104 W Cary St.',
                 'plank_clue': 'Play through one game of "Codenames". You might have to ask to be seated. Afterwards, and ONLY afterwards, tell the staff you\'ve finished playing.',
                 'plank_prompt': 'Answer the plank for your next location.',
                 'name_of_establishment': 'One Eyed Jacques',
                 'plank_answer': 'Rains of Castamere',
                 'is_current': False,
                 'location_complete': False}
place_array[5] = {'place_id': 6,
                 'next_id': 7,
                 'instructions': 'Next address is 3120 W Cary St.',
                 'plank_clue': 'Have a drink! And grab another bite to eat if you\'re hungry.',
                 'plank_prompt': 'Answer the plank in only two words for your next location:',
                 'name_of_establishment': 'Can Can Brasserie',
                 'plank_answer': 'Musical Box',
                 'is_current': False,
                 'location_complete': False}
place_array[6] = {'place_id': 7,
                 'next_id': 0,
                 'instructions': 'Next address is 3005 W Cary St.',
                 'plank_clue': 'Find a plush/fluffy, small, narwhal. There are many narwhals in this place, do not be fooled. Find the small stuffed animal variety and bring it to the counter.',
                 'plank_prompt': 'Answer the plank for your next locations:',
                 'name_of_establishment': 'World of Mirth',
                 'plank_answer': 'Standard Deviation',
                 'is_current': False,
                 'location_complete': False}



superUser = 'super1'
superUserEmail = 'none@none.com'
superUserPass = 'super1super'


#########  CREATE PLACES  #############

for place in place_array:
    if not Place.objects.filter(name_of_establishment=place['name_of_establishment']).exists(): #if the user does not exist
        newPlace = Place.objects.create(
        place_id = place['place_id'],
        next_id = place['next_id'],
        instructions = place['instructions'],
        plank_clue = place['plank_clue'],
        plank_prompt = place['plank_prompt'],
        name_of_establishment = place['name_of_establishment'],
        plank_answer = place['plank_answer'],
        is_current = place['is_current'],
        location_complete = place['location_complete']
        )
        newPlace.save()
        print('(ADDED) ' + newPlace.name_of_establishment)
    else: #if the user does exist
        existingPlace = Place.objects.get(name_of_establishment=place['name_of_establishment'])
        print(existingPlace.name_of_establishment + ' exists already')


#########  CREATE SUPERUSERS  #############
print('------------------')
print('Superusers:\n')
if not User.objects.filter(username=superUser).exists(): #if the user does not exist
    user = User.objects.create_superuser(username=superUser, email = superUserEmail,  password=superUserPass)
    user.save()
    print('(ADDED) ' + str(user) + ' / password is ' + superUserPass)
else: #if the user does exist
    user = User.objects.get(username=superUser)
    print(str(user) + ' already exists')
