import random
import tkinter as tk

# Function to determine if the toast is burnt or not.
# Dynamic weights (0.2 - (better_chance * 0.05), 0.8 + (better_chance * 0.05))
def burnt_toast():
    burn_chances = max(0.05, 0.25 - (better_chance * 0.05))
    tell = random.choices(["burnt", "not burnt"], weights=(burn_chances, 1 - burn_chances), k=1)[0]
    return tell == "burnt"

# A mood function to give different responses based on mood.
def answer_mood():
    t_mood = ["happy", "sad", "excited", "bored", "angry", "evil", "confused", "sleepy", "friendly", "silly"]
    answer = random.choices(t_mood, weights=(5, 5, 5, 5, 5, 1, 5, 5, 5, 5), k=1)[0]
    if answer == "happy":
        print(f"Life’s too short not to enjoy toast. Here you go, {name}!")
    elif answer == "sad":
        print(f"I saved this toast just for you, {name}. Hope it helps a little.")
    elif answer == "excited":
        print(f"Yesss! Toast party for you, {name}!")
    elif answer == "bored":
        print(f"Another toast… yawn… here you go, {name}.")
    elif answer == "angry":
        print(f"Ugh, fine, here’s your toast {name}. Happy now?")
    elif answer == "evil":
        print(f"Oops, no toast for you, {name}… I ate it all! Muahaha!")
    elif answer == "confused":
        print(f"Wait… did you ask for toast, {name}? Or was it cookies?")
    elif answer == "sleepy":
        print(f"Zzz… oh, right. Here’s your toast, {name}. Don’t wake me up again!")
    elif answer == "friendly":
        print(f"Sharing is caring! A toast for you, {name}, from the heart!")
    elif answer == "silly":
        print(f"Here’s your toast, {name}… with invisible butter!")

# Function to display a random game over message.
def game_over():
    message = ["The toaster exploded dramatically!, see ya next time!", "All the bread has been stolen by pigeons!, see ya next time!", "I accidentally set the kitchen on fire!, see ya next time!", "A mysterious toast thief has taken all your bread!, see ya next time!", "The toaster has gone on strike!, see ya next time!"]
    return random.choice(message)

# Silly nickname for the player.
def nickname():
    nicknames = ["Toastmaster", "Bread Baron", "Crumb Commander", "Slice Sultan", "Toasty Titan", "Butter Boss", "Jam Jester", "Crunch Captain", "Loaf Legend", "Yeast Yoda"]
    return random.choice(nicknames) + f" {name}"

# Get user's name.
name = input("What is your name? ")
print("Right now you've got 25% chance of burning your toast.")

# Loop continues until the user enters 'n' to exit.
better_chance = 0
points = 0
lives = 3
burn = 0
not_burn = 0

while True:
    question = input(f"Do you want a toast, {name}? (y/n): ")
    if question.lower() == 'y':
        if burnt_toast():
            print(f"Your toast is burnt, you've got")
            burn += 1
            lives -= 1
            if lives == 0:
                print(game_over())
                print(f"Total toasts made: {burn + not_burn}")
                break
            print(f"Oh no! The toast is burnt! Lives left: {lives}")
            print(f"Burnt toasts: {burn}, Not burnt toasts: {not_burn}")
        else:
            not_burn += 1
            points += 1
            answer_mood()
            print(f"Burnt toasts: {burn}, Not burnt toasts: {not_burn}")
    elif question.lower() == 'n':
        print(f"Burnt toasts: {burn}, Not burnt toasts: {not_burn}")
        break
    else:    
        print("Just use y/n next time.")
        continue
    # Upgrade system
    if points >= 10:
        need_upgrade = input("Do you want to buy an upgrade for 10 points? (y/n): ")
        if need_upgrade.lower() == 'y':
                choose = input("Do you want more lives or a better chance of not burning toast? (l/c): ")
        if choose.lower() == 'l':
            lives += 1
            points -= 10
            print(f"You now have {lives} lives. Points left: {points}")
        elif choose.lower() == 'c':
            better_chance += 1
            points -= 10
            burn_percent = max(5, int((0.25 - (better_chance * 0.05)) * 100))
            print(f"Your chance of not burning toast has improved! Points left: {points}")
        else:
            print("Ok, maybe next time.")
        