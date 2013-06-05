# Source File Name: slotmachine.py
# Author's Name: Jonathan Hodder
# Last Modified By: Jonathan Hodder
# Date Last Modified: Monday June 3rd, 2013
#Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
#for the user that is an image of a slot machine with Label and Button objects

#Version: 0.1 - Original code provided from Teacher. 
#(Contains the framework for the slot machine)
#Version: 0.2 - Added pygame import and other pygame code from lesson 4.
#Version: 0.3 - Added default spin image and slot machine background.
                
# import statements
import random
import pygame
pygame.init()

def Reels():
    """ When this function is called it determines the Bet_Line results.
        e.g. Bar - Orange - Banana """
        
    # [0]Fruit, [1]Fruit, [2]Fruit
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "blank.jpg"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "grapes.jpg"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "banana.jpg"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "orange.jpg"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "cherry.jpg"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "bar.jpg"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "bell.jpg"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "seven.jpg"    
           
    return Bet_Line

def is_number(Bet):
    """ This function Checks if the Bet entered by the user is a valid number """
    try:
        int(Bet)
        return True
    except ValueError:
        print("Please enter a valid number or Q to quit")
        return False

def pullthehandle(Bet, Player_Money, Jack_Pot):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    Fruit_Reel = Reels()
    Fruits = Fruit_Reel[0] + " - " + Fruit_Reel[1] + " - " + Fruit_Reel[2]
    
    # Match 3
    if Fruit_Reel.count("grapes.jpg") == 3:
        winnings,win = Bet*20,True
    elif Fruit_Reel.count("banana.jpg") == 3:
        winnings,win = Bet*30,True
    elif Fruit_Reel.count("orange.jpg") == 3:
        winnings,win = Bet*40,True
    elif Fruit_Reel.count("cherry.jpg") == 3:
        winnings,win = Bet*100,True
    elif Fruit_Reel.count("bar.jpg") == 3:
        winnings,win = Bet*200,True
    elif Fruit_Reel.count("bell.jpg") == 3:
        winnings,win = Bet*300,True
    elif Fruit_Reel.count("seven.jpg") == 3:
        print("Lucky Seven!!!")
        winnings,win = Bet*1000,True
    # Match 2
    elif Fruit_Reel.count("blank.jpg") == 0:
        if Fruit_Reel.count("grapes.jpg") == 2:
            winnings,win = Bet*2,True
        if Fruit_Reel.count("banana.jpg") == 2:
            winnings,win = Bet*2,True
        elif Fruit_Reel.count("orange.jpg") == 2:
            winnings,win = Bet*3,True
        elif Fruit_Reel.count("cherry.jpg") == 2:
            winnings,win = Bet*4,True
        elif Fruit_Reel.count("bar.jpg") == 2:
            winnings,win = Bet*5,True
        elif Fruit_Reel.count("bell.jpg") == 2:
            winnings,win = Bet*10,True
        elif Fruit_Reel.count("seven.jpg") == 2:
            winnings,win = Bet*20,True
    
        # Match Lucky Seven
        elif Fruit_Reel.count("seven.jpg") == 1:
            winnings, win = Bet*10,True
            
        else:
            winnings, win = Bet*2,True
    if win:    
        print(Fruits + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
        Player_Money += int(winnings)
    
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        if  jackpot_try  == jackpot_win:
            print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
            Jack_Pot = 500
        elif jackpot_try != jackpot_win:
            print ("You did not win the Jackpot this time. \nPlease try again ! \n")
    # No win
    else:
        print(Fruits + "\nPlease try again. \n")
    
    return Player_Money, Jack_Pot, win

def main():
    """ The Main function that runs the game loop """
    #D - Display Config
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("U Got Died Slot Machine")

    #E - Entities (add slot machine template)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("slotMachineTemplate.jpg")
    #load the default image 
    slot = pygame.Surface((200, 200))
    slot = slot.convert()
    slot = pygame.image.load("spin.jpg")
    #load the blank image
    blank = pygame.Surface((200, 200))
    blank = blank.convert()
    blank = pygame.image.load("blank.jpg")
    #load the grapes image
    grapes = pygame.Surface((200, 200))
    grapes = grapes.convert()
    grapes = pygame.image.load("grapes.jpg")
    #load the banana image
    banana = pygame.Surface((200, 200))
    banana = banana.convert()
    banana = pygame.image.load("banana.jpg")
    #load the orange image
    orange = pygame.Surface((200, 200))
    orange = orange.convert()
    orange = pygame.image.load("orange.jpg")
    #load the cherry image
    cherry = pygame.Surface((200, 200))
    cherry = cherry.convert()
    cherry = pygame.image.load("cherry.jpg")
    #load the bar image
    bar = pygame.Surface((200, 200))
    bar = bar.convert()
    bar = pygame.image.load("bar.jpg")
    #load the bell image
    bell = pygame.Surface((200, 200))
    bell = bell.convert()
    bell = pygame.image.load("bell.jpg")
    #load the seven image
    seven = pygame.Surface((200, 200))
    seven = bar.convert()
    seven = pygame.image.load("seven.jpg")
    
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 0
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    
    # Flag to initiate the game loop
    clock = pygame.time.Clock()
    KeepGoing = True
    
    while KeepGoing == True:
        #T - Timer to set frame rate
        clock.tick(30)
        win = 0
        # Give the player some money if he goes broke
        #if Player_Money <1:
        #    input("You have no more money. Here is $500 \nPress Enter\n")
        #    Player_Money = 500
        #Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                KeepGoing = False
        #R - Refresh display
        screen.blit(background, (0, 0))
        screen.blit(slot, (25, 30))
        screen.blit(slot, (225, 30))
        screen.blit(slot, (425, 30))
        pygame.display.flip()
        
        #if Prompt == "" and Turn >1:
        #    Bet = Prev_Bet
        #    print("Using Previous Bet")
        #    if Bet > Player_Money:
        #        print("Sorry, you only have $" + str(Player_Money) + " \n")
        #    elif Bet <= Player_Money:
        #        Turn +=1
        #        Prev_Bet = Bet
        #        Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        
        #elif is_number(Prompt ):
        #   Bet = int(Prompt )
            # not enough money
        #    if Bet > Player_Money:
        #        print("Sorry, you only have $" + str(Player_Money) + " \n")
                
        #    # Let's Play
        #    elif Bet <= Player_Money:
        #        Turn +=1
        #        Prev_Bet = Bet
        #        Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        #
        # determine win/loss ratio for debugging purposes
        #if win:
        #    win_number += 1
        #else:
        #    loss_number += 1
        #win_ratio = "{:.2%}".format(win_number / Turn)
        #print("Wins: " + str(win_number) + "\nLosses: " + str(loss_number) + "\nWin Ratio: " + win_ratio + "\n")           
        #       
        #    
    #The End
    print("- Program Terminated -")
    
if __name__ == "__main__": main()