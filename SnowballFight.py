''' 
    Name: Snowball-Mania
    Author: Kyle Yeh
    Date: December 5, 2025
    Class: AP Computer Science Principles
    Python: 3.13
'''

import random
import time
from colorama import *
from tkinter import *

screen = Tk()
frame1 = Frame(screen, width=600, height=600)
frame1.pack()
welcomeText = Label(frame1, text='Follow the instructions on the terminal. Thank you for shopping with us.')
welcomeText.pack()

kills = {}

init()

def printIntro():
    '''
    ' Param: none
    ' 
    ' Print a welcome message to the user
    ' 
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("❄️  Welcome to Snowball Mania!❄️")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def getNames():
    '''
    ' Param: none
    ' 
    ' Create a list to hold player names.
    ' Ask the user for their name.  Store it in a variable and add it to the player list.
    ' Print instructions for the user to add more players and to type "DONE" when finished.
    ' Read in the first additional player name.
    ' While the user hasn't typed "DONE", add the new name to the player list and prompt for the next name
    ' After the user is finished entering names, print a "Time to play!" message
    '
    ' Return: the list of player names
    ' 
    '''
    playerList = []
    myName = input("What is your name? ")
    playerList.append(myName)
    myName = input("Add other players (one at a time) by typing their names and hitting ENTER. To stop entering names, type 'DONE'. ")
    while myName != "DONE":
        playerList.append(myName)
        myName = input("Add other players (one at a time) by typing their names and hitting ENTER. To stop entering names, type 'DONE'. ")
    print("Great - time to play!")
    return playerList

def getThrower(players):
    '''
    ' Param: players (list of player names)
    '
    ' Return a randomly chosen player name to be the next thrower.
    '
    ' Return: player name
    '''
    thrower = random.choice(players)
    return thrower

    
def getVictim(players, t):
    '''
    ' Param: players (list of player names), t (the thrower for this round)
    ' 
    ' Select a random player to be the next victim.  
    ' While the victim is the same player as the thrower, randomly select a new victim from the list.
    ' Return the victim's name.
    '
    ' Return: victim's name
    '''
    victim = random.choice(players)
    while (t == victim):
        victim = random.choice(players)
    return victim


def getHitResult():
    '''
    ' Param: none
    ' 
    ' Generate a random number between 1 and 10
    ' If the number is greater than 4 (60% chance), return True
    ' Else, return False
    '
    ' Return: Boolean representing whether or not the snowball hit
    '''
    hitNum = random.randint(1, 10)
    if (hitNum > 4):
        return True
    else:
        return False
    

def playSnowballFight(players):
    '''
    ' Param: players (a list of players still in the game)
    '
    ' While there are still multiple players in the game...
    '   - Get the next thrower
    '   - Get the next victim
    '   - Get the next hit result
    '   - If a hit occurred, flip a coin to see if it is a knockout or not.
    '     - If knockout, print a knockout message and remove the victim from the list
    '     - Else, print a hit message but do not remove victim
    '   - Else, print a miss message
    '   - time.sleep(3) - delay execution for three seconds
    ' 
    ' Return: none
    '''
    init()

    while (len(players) > 1):
        thrower = getThrower(players)
        victim = getVictim(players, thrower)
        hitResult = getHitResult()

        survives1 = Fore.YELLOW + thrower + " throws at " + victim + " and hits, but " + victim + " survives!"
        survives2 = Fore.YELLOW + thrower + " throws at " + victim + " and hits, but the snowball bounces off and " + victim + " is still standing like a statue!"
        survives3 = Fore.YELLOW + thrower + " throws at " + victim + " and makes contact... with " + victim + "'s hand! Steeeeeee-rike!"

        ko1 = Fore.RED + thrower + " throws and absolutely destroys " + victim + " - " + victim + " is out of the game!!!"
        ko2 = Fore.RED + thrower + " throws and murders " + victim + " with an ice ball - " + victim + " is now dead, and " + thrower + " is now wanted."

        if (hitResult == True):
            koResult = random.randint(1, 2)     # 1 = not KO, 2 = KO
            if (koResult == 1):
                print(random.choice([survives1, survives2, survives3]))
                kills[thrower] = (kills[thrower] + 1 if thrower in kills else 1)
            else:
                print(random.choice([ko1, ko2]))
                players.remove(victim)
        else:
            print(Fore.GREEN + thrower + " throws at " + victim + " but has really bad aim and misses.")
        time.sleep(0.5)
    
def printOutro(winner):
    '''
    ' Param: name of the winner
    ' 
    ' Print a congratulatory message naming the winner
    '
    ' Return: none
    '''
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")
    print("All hail " + winner + ", the Ultimate Student/Snowball Wizard!")
    print("❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️❄️")


def runProgram():
    '''
    ' Param: none
    ' 
    ' Call the method that will print the intro messages
    ' Call the method that will return a list of player names.  Save the list in a variable.
    ' Call the method that will simulate the snowball fight
    ' Call the method that will print the outro messagees
    '
    ' Return: none
    '''
    printIntro()
    testPlayers = getNames()
    for widget in frame1.winfo_children():
        widget.destroy()
    inProgressMessage = Label(frame1, text="Snowball fight in progress. No kills yet!")
    inProgressMessage.pack()
    playSnowballFight(testPlayers)
    printOutro(testPlayers[0])


runProgram()


testPlayers = ["Jack", "Sam", "Eliana", "Aanya", "Izaiah", "Audrey", "Elam", "John", "Jared", "Aron", "Sebastien", "Tyler", "Collin", "Taylor", "Will", "Nolan", "Llyden", "Xavier", "Landon", "Mr. Holthouse", "Mr. Yeh", "Everett"]
playSnowballFight(testPlayers)
printOutro(testPlayers[0])
# testThrower = getThrower(testPlayers)
# testVictim = getVictim(testPlayers, testThrower)
# testHit = getHitResult()

# # successful hit
# if (testHit == True):
#     print(testThrower + " throws at " + testVictim + " - HIT")
# # miss
# else:
#     print(testThrower + " throws at " + testVictim + " - MISS")

