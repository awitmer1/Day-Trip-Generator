"""
(5 points): As a developer, I want to make at least three commits with descriptive messages 

(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, 
and entertainment in their own separate Lists. (String Values)(at least 4)

(5 points): As a user, I want a destination to be randomly selected for my day trip. 

(5 points): As a user, I want a restaurant to be randomly selected for my day trip

(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 

(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, 
and/or form of entertainment if I dont like one or more of those things.

(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

(10  points): As a user, I want to display my completed trip in the console

(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing! 
"""

import random

destination_list = ["Tatooine", "Hoth", "Coruscant", "Endor", "Tython", "Geonosis", "Korriban", "Mandalore"]

restaurant_list = ["Mos Eisley Cantina", "Canto Bight Casino", "Lars Family Homestead", "Dex's Restaurant", "Ewok Treetop Village"]

transportation_list = ["Tantive IV", "Millenium Falcon", "Slave I", "Home One", "Executor", "Invisible Hand", "Scimitar"]

entertainment_list = ["Twi'lek Dance Party", "Round of Sabaac", "Ewok BBQ", "Kessel Run", "Beggars Canyon Target Practice"]



def itinerary():
    print("Here is your day trip in a galaxy far, far away...")
    random_destination()
    random_restaurant()
    random_transportation()
    random_entertainment()
    user_satisfaction()
    
def random_destination():
    for dest in destination_list:
        location = random.choice(destination_list)
    print(f"Location: {location}")

def random_restaurant():
    for rest in restaurant_list:
        restaurant = random.choice(restaurant_list)
    print(f"Restaurant: {restaurant}")

def random_transportation():
    for trans in transportation_list:
        transportation = random.choice(transportation_list)
    print(f"Transport: {transportation}")

def random_entertainment():
    for ent in entertainment_list:
        entertainment = random.choice(entertainment_list)
    print(f"Entertainment: {entertainment}")

def user_satisfaction():
    user_input = input(f"Are you happy with this itinerary? y/n")
    if user_input == "n":
            make_changes()
    else:
        print("Enjoy your trip! Watch out for Jawas!") 

def make_changes():
    change_desired = input(f"What would you like to change? Destination, Restaurant, Transportation, Entertainment")
    if change_desired == "Destination":
        destination_satisfaction()
    elif change_desired == "Restaurant":
        restaurant_satisfaction()
    elif change_desired == "Transportation":
        transportation_satisfaction()
    elif change_desired == "Entertainment":
        entertainment_satisfaction()
    else:
        print("Sorry, please try that again...")       

def destination_satisfaction():
    dest_sat = False
    while dest_sat == False:
        random_destination()
        destination_change = input(f"Does this sound better to you? y/n")
        if destination_change == "y":
            dest_sat = True
    else:
        dest_sat = True
        print("Great! Let's update that itinerary.")

def restaurant_satisfaction():
    rest_sat = False
    while rest_sat == False:
        random_restaurant()
        restaurant_change = input(f"Does this sound better to you? y/n")
        if restaurant_change == "y":
            rest_sat = True
    else:
        rest_sat = True
        print("Great! Let's update that itinerary.")

def transportation_satisfaction():
    trans_sat = False
    while trans_sat == False:
        random_transportation()
        transportation_change = input(f"Does this sound better to you? y/n")
        if transportation_change == "y":
            trans_sat = True
    else:
        trans_sat = True
        print("Great! Let's update that itinerary.")

def entertainment_satisfaction():
    ent_sat = False
    while ent_sat == False:
        random_entertainment()
        entertainment_change = input(f"Does this sound better to you? y/n")
        if entertainment_change == "y":
            ent_sat = True
    else:
        ent_sat = True
        print("Great! Let's update that itinerary.")
    
itinerary()