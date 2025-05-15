# -*- coding: utf-8 -*-
"""
CPS109 - Section 03
Logan Toy
11/24/2024 

The program should implement a minigame selector where you could play different games
with the computer or with another person. The program should have the following games and features:

Mastermind
    Game where you have to guess an unknown order of 4 colours.
    The player is given info on how many colours that the player chose are in the order
    and how many are in the right spot, but not which ones specifically.
    The game should have a single player version, where the order is chosen by the program
    and a two player version, where the second player can choose it.
    The game will then output the final display to a file.
        
Wordle
    Hit internet game where you guess a pre-set 5-letter word.
    Tells the player with specific letters are correct, and which are in the word but out of place.
    The game should have a single player version, where the word is chosen by reading from a file,
    and two player version where the second player chooses the word.
    The game will then output the final display to a file.
    

External Features
    Ability To Exit Program
    When selecting game, loops until exit
        
"""

#Imports
import time
import random

#----------------------- MASTERMIND -------------------

#Function to loop if input contains invalid letter
def invalidLetter(inputedOrder):
    for i in range(len(inputedOrder)):
        if inputedOrder[i] not in "roygbpwkn":
            return True
    return False
#End of invalidLetter


#Mastermind Function      
def mastermind():
    #Conversion Dict
    mdict = {
            "r":"🔴",
            "o":"🟠",
            "y":"🟡",
            "g":"🟢",
            "b":"🔵",
            "p":"🟣",
            "w":"⚪",
            "k":"⚫",
            "n":"🟤"
            }
    playerCount = ":)"
    while playerCount != "1" and playerCount != "one" and playerCount != "2" and playerCount != "two":
        print("1 or 2 players?:\n(In 2-player, the second person picks the order)")
        print("1) One")
        print("2) Two")
        print("3) Instructions")
        playerCount = input("> ").lower()
        
        
        #Player Count Checker
        if playerCount == "1" or playerCount == "one": #One Player
            colours = "🔴🟠🟡🟢🔵🟣⚪⚫🟤"
            chosenOrder = colours[random.randint(0,8)]+colours[random.randint(0,8)]+colours[random.randint(0,8)]+colours[random.randint(0,8)]
            print("The order has been chosen")
            
        elif playerCount  == "2" or playerCount == "two": #Two Player
            print("Player 2, please input a 4-colour order:")
            print("The colours are:")
            print("🔴=r  🟠=o  🟡=y  🟢=g  🔵=b  🟣=p  ⚪=w  ⚫=k  🟤=n")
            userOrder = input("> ").lower()
            while not userOrder.isalpha() or len(userOrder) != 4 or invalidLetter(userOrder):
                print("Invalid Input.")
                time.sleep(0.25)
                print("Player 2, please input a 4-colour order:")
                userOrder = input("> ").lower()
            chosenOrder = "".join([mdict[x] for x in userOrder])
            print("Your chosen order is:",chosenOrder)
            print("Now hiding chosen order...\n(Please manually scroll to further hide it)")
            time.sleep(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Please give the device to Player 1")
            
        elif playerCount  == "3" or playerCount == "instructions": #Instructions
            print("Mastermind is a a guessing game.")
            print("You have to guess in 10 rounds the 4-slot colour order by guessing your own colour order.")
            print("A \"●\" means one of the colours is in the right slot.")
            print("A \"○\" means one of the colours is in the order, but not in the right slot")
            print("Note the fact that in the order, colours can repeat.")
            print("Have fun!\n")
            time.sleep(2)
        else:
            print("Invalid Input.")
     #End of Player Loop
    
    
    time.sleep(1)
    finalGame = "\n"
 
    #Round Looping
    for runCount in range(11):
        #End if unsuccessful
        if runCount == 10:
            print("Whomp whomp... \nYou failed to guess the order:",chosenOrder)
            break
        
        #Run a turn
        returnedTurn = mastermindTurn(runCount,chosenOrder,finalGame,mdict)
        
        #Win Checker
        if returnedTurn[0:4] == chosenOrder:
            print("Congratulations!!!\nYou guess the order:",chosenOrder)
            finalGame = (finalGame+returnedTurn+"\n")
            break
        else:
            finalGame = (finalGame+returnedTurn+"\n")
    #End of Turn For Loop

    print("\n\n")
    return chosenOrder+"\n----------"+finalGame
#End of Mastermind


def mastermindTurn(runCount,chosenOrder,finalGame,mdict):

    print()
    print("Turn", runCount+1,"of 10")
    print("Player, make your guess")
    print("The colours are:")  
    print("🔴=r  🟠=o  🟡=y  🟢=g  🔵=b  🟣=p  ⚪=w  ⚫=k  🟤=n")
    guessOrder = input("> ").lower()
    #Invalid Input Loop
    while not guessOrder.isalpha() or len(guessOrder) != 4 or invalidLetter(guessOrder):
        print("Invalid Input.")
        time.sleep(0.25)
        print("Player, make your guess")
        guessOrder = input("> ").lower()
    #End of invalid input loop
     
    #Savestates for checking values
    checkTurn = [None, None, None, None]
    scanned = [False,False,False,False]
    
    #Counting each item thats correct
    for i in range(4):
        if mdict[guessOrder[i]] == chosenOrder[i]:
            checkTurn[i] = "correct"
            scanned[i] = True
    
    #Counting each item thats wrong slot, but in the order
    for i in range(4):
        for j in range(4):
            if mdict[guessOrder[i]] == chosenOrder[j] and scanned[j] == False and checkTurn[i] != "correct":
                checkTurn[i] = "included"
                scanned[j] = True
                break
    
    #Create returning answers
    answers = ""
    for i in range(4):
        if checkTurn[i] == "correct":
            answers += "●"
    for i in range(4):
        if checkTurn[i] == "included":
            answers += "○"
            
    #Output guess result with guess, answer outputs, and past turns
    print(finalGame+"".join([mdict[x] for x in guessOrder])+"   "+answers+"\n")
  
    return "".join([mdict[x] for x in guessOrder])+"   "+answers
#End of mastermindTurn Function
#---------------------------------------------------------------



#----------------------- WORDLE -------------------
#Wordle Function      
def wordle():
    playerCount = ":)"
    #Player Loop
    while playerCount != "1" and playerCount != "one" and playerCount != "2" and playerCount != "two":
        print("1 or 2 players?:\n(In 2-player, the second person picks the word)")
        print("1) One")
        print("2) Two")
        print("3) Instructions")
        playerCount = input("> ").lower()
        
        #Player Count Check
        if playerCount == "1" or playerCount == "one": #One Player
            chosenIndex = random.randint(0,2308)
            wordfile = open("wordlewords.txt","r")
            content = wordfile.readlines()
            chosenWord = content[chosenIndex]
            print("The word has been chosen")
            
        elif playerCount  == "2" or playerCount == "two": #Two Player
            print("Player 2, please input a 5-letter word:")
            chosenWord = input("> ").upper()
            while not chosenWord.isalpha() or len(chosenWord) != 5:
                print("Invalid Input.")
                time.sleep(0.25)
                print("Player 2, please input a 5-letter word:")
                chosenWord = input("> ").upper()
            print("Your chosen word is:",chosenWord)
            print("Now hiding chosen word...\n(Please manually scroll to further hide it)")
            time.sleep(3)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("Please give the device to Player 1")
            
        elif playerCount  == "3" or playerCount == "instructions": #Instructions
            print("Wordle is played with 5-letter words.")
            print("You have to guess in 6 rounds the selected word by guessing your own words.")
            print("A \"🟩\" means the letter is in the right slot.")
            print("A \"🟨\" means the letter is in the word, but not in that slot.")
            print("A \"⬜\" means the letter is not contained in the word.")
            print("Have fun!\n")
            time.sleep(2)
     #End of Player Loop
    
    time.sleep(1)
    finalGame = "\n"
    
    #Run each round
    for runCount in range(7):
        #Ran out of turns
        if runCount == 6:
            print("Whomp whomp... \nYou failed to guess the word:",chosenWord)
            break
        #Run a turn
        returnedTurn = wordleTurn(runCount,chosenWord,finalGame)
        if "🟨" not in returnedTurn and "⬜" not in returnedTurn:
            print("Congratulations!!!\nYou guess the word:",chosenWord)
            finalGame = (finalGame+returnedTurn+"\n")
            break
        else:
            finalGame = (finalGame+returnedTurn+"\n")
    #End of Turn For Loop
    
    print("\n\n")
    return chosenWord+finalGame
#End of Wordle

def wordleTurn(runCount,chosenWord,finalGame):
    print()
    print("Turn", runCount+1,"of 6")
    print("Player, make your guess")
    guessWord = input("> ").upper()
    while not guessWord.isalpha() or len(guessWord) != 5:
        print("Invalid Input.")
        time.sleep(0.25)
        print("Player, make your guess")
        guessWord = input("> ").upper()
    #End of invalid input loop
     
    #Savestates for checks
    currentTurn = [None, None, None, None, None]
    scanned = [False,False,False,False,False]
    
    #Check for green 2
    for i in range(5):
        if guessWord[i] == chosenWord[i]:
            currentTurn[i] = "🟩"+guessWord[i]+" "
            scanned[i] = True
    
    #Check for yellow
    for i in range(5):
        for j in range(5):
            if guessWord[i] == chosenWord[j] and scanned[j] == False and type(currentTurn[i]) != str:
                currentTurn[i] = "🟨"+guessWord[i]+" "
                scanned[j] = True
                break
    
    #Fill gaps with white
    for i in range(5):
        if currentTurn[i] == None:
            currentTurn[i] = "⬜"+guessWord[i]+" "
    
    #Combine the list
    currentTurnOutput = " ".join(currentTurn)
    
    #Output guess result, with previous turns
    print(finalGame+currentTurnOutput+"\n")
  
    return currentTurnOutput
#End of wordleTurn Function
#-----------------------------------------------------------

#----------------- MAIN GAME RUNNER ------------------------
#Boolean to loop selector
loopProgram = True

while loopProgram:
    #Print out info on game choices
    print("PLease select one of the following games:")
    print("1) Mastermind")
    print("2) Wordle")
    print("0) Exit")
    
    #Take input and covert to lowercase
    gameChoice = input("> ").lower()
    
    #Mastermind
    if gameChoice == "1" or gameChoice == "mastermind":
        print("Now playing... Mastermind\n")
        time.sleep(1)
        outputedGame = mastermind() #Run Game
        with open("gamedisplay.txt","w") as file: #Write game to file
            file.write(outputedGame)
        print("Game has been outputed to \"gamedisplay.txt\"")
        time.sleep(5)
        
    #Wordle
    elif gameChoice == "2" or gameChoice == "wordle":
        print("Now playing... Wordle\n")
        time.sleep(1)
        outputedGame = wordle() #Run Game
        with open("gamedisplay.txt","w") as file: #Write game to file
            file.write(outputedGame)
        print("Game has been outputed to \"gamedisplay.txt\"")
        time.sleep(5)
        
    #Exit and Error
    elif gameChoice == "0" or gameChoice == "exit": 
        loopProgram = False
        print("Thank you for playing!")
    else:
        print("This does not seem to be any of the possible options. :(\nPlease try again.\n\n")        
#End of while loop
#-----------------------------------------------------------------------

        
        
        
        
        
        