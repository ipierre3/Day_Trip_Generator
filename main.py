# Main Stories
 
# (5 points): As a developer, I want to make at least three commits with descriptive messages 
# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
# (10  points): As a user, I want to display my completed trip in the console
# (5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 

import random

destination_list = ['Maldives', 'Paris', 'Maui', 'Tokyo', 'Rome']
destination = random.choice(destination_list)

mode_of_transportation = ['taxi', 'bus', 'cycle', 'ferry', 'rental car', 'train', 'metro', 'ride-sharing']
mode_of_transportation1 = random.choice(mode_of_transportation)

restaurant_maldives = ['Ithaa Undersea Restaurant', 'REETHI Restaurant', 'M6M Restaurant', 'Bokkura Restaurant', 'Symphony Restaurant']
restaurant1 = random.choice(restaurant_maldives)
restaurant_paris = ['Bistrot Alexandre III', 'Restaurant Guy Savoy', 'Epicure', 'ASPIC', 'La Table de Colette']
restaurant2 = random.choice(restaurant_paris)
restaurant_maui = ["Zippy's Kahului", "Lahaina Grill", "Kimo's Maui", "Mama's Fish House", "Morimoto Maui"]
restaurant3 = random.choice(restaurant_maui)
restaurant_tokyo = ["Narisawa", "Ise Sueyoshi", "L'Effervescence", "Toufuya Ukai", "Kagurazaka Ishikawa"]
restaurant4 = random.choice(restaurant_tokyo)
restaurant_rome = ['Ercoli Trastevere', 'Poldo e Gianna Osteria', 'Roscioli Salumeria con Cucina', 'Retrobottega', 'Roma Sparita']
restaurant5 = random.choice(restaurant_rome)

entertainment_maldives = ['Whale & Dolphin Watching', 'Diving', 'Snorkeling']
entertainment1 = random.choice(entertainment_maldives)
entertainment_paris = ['the Eifel Tower', 'the Louvre', 'the Notre Dame', 'the Arc de Triomphe']
entertainment2 = random.choice(entertainment_paris)
entertainment_maui = ['the Molokai', 'the Lanai', 'the Kahoolawe']
entertainment3 = random.choice(entertainment_maui)
entertainment_tokyo = ['the Tokyo Sky Tree', 'Shibuya', 'the Meiji Shrine', 'Tokyo Royal Palace']
entertainment4 = random.choice(entertainment_tokyo)
entertainment_rome = ['the Colosseum' , 'the Piazza Navona', 'the Vatican museums']
entertainment5 = random.choice(entertainment_rome)


greeting = "Welcome to the Day Trip Generator! If you aren't sure what you want to do for your vacation, you have come to the right place!"
print (greeting)

print('We have selected' + ' ' + random.choice(destination_list) + ' ' + 'for your destination! Does this sound good?')

def user_answer(user_choice):
    destination = random.choice(destination_list)
    for choice in user_choice:
        if choice == 'y':
            print("Awesome! Glad that is decided let's move on!")
        elif choice == 'n':
            print(f"Oh, sorry you don't like this destination. No worries, we can try something else! How about {destination}?")
            user_answer(input('Enter y/n: '))
    return destination

user_answer(input('Enter y/n: '))
chosen_destination = destination

print('We have selected' + ' ' + mode_of_transportation1 + ' ' + 'for your transportation option! Does this sound good?')

def user_answer2 (user_choice2):
    for choice in user_choice2:
        transportation = mode_of_transportation1
        if choice == 'y':
            print("Awesome! Glad that is decided let's move on!")
        elif choice == 'n':
            print(f"Oh, sorry you don't like this transportation option. No worries, we can try something else! How about {random.choice(mode_of_transportation)}?")
            user_answer2(input('Enter y/n: '))
    return transportation

user_answer2(input('Enter y/n: '))

destination = format(random.choice(destination_list))

for chosen_destination in destination:
    if destination == 'Maldives':
        print('We have selected' + ' ' + entertainment1  + ' ' + 'for your entertainment option! Does this sound good?')
        user_answer3 = (input('Enter y/n: '))
        if user_answer3 == 'y':
            print("Awesome! Glad that is decided let's move on!")
        elif user_answer3 == 'n':
            print((f"Oh, sorry you don't like this entertainment option. No worries, we can try something else! How about {random.choice(entertainment1)}?"))
            user_answer3 = (input('Enter y/n: '))
    if destination == 'Paris':
        print('We have selected' + ' ' + entertainment2  + ' ' + 'for your entertainment option! Does this sound good?')
        user_answer3 = (input('Enter y/n: '))
        if user_answer3 == 'y':
                print("Awesome! Glad that is decided let's move on!")
        elif user_answer3 == 'n':
            print((f"Oh, sorry you don't like this entertainment option. No worries, we can try something else! How about {random.choice(entertainment2)}?"))
            user_answer3 = (input('Enter y/n: '))
    if destination == 'Maui':
        print('We have selected' + ' ' + entertainment3  + ' ' + 'for your entertainment option! Does this sound good?')
        user_answer3 = (input('Enter y/n: '))
        if user_answer3 == 'y':
                print("Awesome! Glad that is decided let's move on!")
        elif user_answer3 == 'n':
            print((f"Oh, sorry you don't like this entertainment option. No worries, we can try something else! How about {random.choice(entertainment3)}?"))
            user_answer3 = (input('Enter y/n: '))
    if destination == 'Tokyo':
        print('We have selected' + ' ' + entertainment4  + ' ' + 'for your entertainment option! Does this sound good?')
        user_answer3 = (input('Enter y/n: '))
        if user_answer3 == 'y':
                print("Awesome! Glad that is decided let's move on!")
        elif user_answer3 == 'n':
            print((f"Oh, sorry you don't like this entertainment option. No worries, we can try something else! How about {random.choice(entertainment4)}?"))
            user_answer3 = (input('Enter y/n: '))
    if destination == 'Rome':
        print('We have selected' + ' ' + entertainment5  + ' ' + 'for your entertainment option! Does this sound good?')
        user_answer3 = (input('Enter y/n: '))
        if user_answer3 == 'y':
                print("Awesome! Glad that is decided let's move on!")
        elif user_answer3 == 'n':
            print((f"Oh, sorry you don't like this entertainment option. No worries, we can try something else! How about {random.choice(entertainment5)}?"))
            user_answer3 = (input('Enter y/n: '))
