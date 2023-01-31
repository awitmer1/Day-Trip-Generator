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

def user_satisfaction():
    user_input = input(f"Are you happy with this itinerary? y/n")
    if user_input == "n":    
        desired_change = input(f"What would you like to change? Destination, Restaurant, Transportation, Entertainment")
        if desired_change == "Destination":
            random_destination()
        elif desired_change == "Restaurant":
            random_restaurant()
        elif desired_change == "Transportation":
            random_transportation()
        elif desired_change == "Entertainment":
            random_entertainment()
        else:
            print("Please try that again...")
    else:
        print("Enjoy your trip! Watch out for Jawas!") 

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


itinerary()