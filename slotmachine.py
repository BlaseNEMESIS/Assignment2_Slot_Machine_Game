# Source File Name: slotmachine.py
# Author's Name: Jonathan Hodder
# Last Modified By: Jonathan Hodder
# Date Last Modified: Monday June 3rd, 2013
#Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
#for the user that is an image of a slot machine with Label and Button objects  
#Allows the user to bet and then spin the slot machine.  You can either win something 

#Version: 0.1 - Original code provided from Teacher. 
#(Contains the framework for the slot machine)
#Version: 0.2 - Added pygame import and other pygame code from lesson 4.
#Version: 0.3 - Added default spin image and slot machine background.
#Version: 0.4 - Finished adding all the labels and buttons.  Still need to add functionality
# and figure out how to create text boxes in Pygame.
#Version: 0.5 - Removed Pygbutton and replaced it with buttons.py
#Completed jackpot message and have slot machine spin working.  
#Need to complete bet validation
                
# import statements
import random
import pygame
import Buttons
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
            Bet_Line[spin] = "luckySeven.jpg"    
           
    return Bet_Line

def is_number(Bet):
    """ This function Checks if the Bet entered by the user is a valid number """
    try:
        int(Bet)
        return True
    except ValueError:
        print("Please enter a valid number or Q to quit")
        return False

def pullthehandle(Player_Money, Bet, Jack_Pot, win, Fruit_Reel):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
    Jack_Pot = Jack_Pot + (Bet*.15) # 15% of the player's bet goes to the jackpot
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
    elif Fruit_Reel.count("luckySeven.jpg") == 3:
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
        elif Fruit_Reel.count("luckySeven.jpg") == 2:
            winnings,win = Bet*20,True
    
        # Match Lucky Seven
        elif Fruit_Reel.count("luckySeven.jpg") == 1:
            winnings, win = Bet*10,True
            
        else:
            winnings, win = Bet*2,True
    if win:    
        Player_Money += int(winnings)
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        
        if  jackpot_try  == jackpot_win:
            Player_Money = Player_Money + Jack_Pot
            Jack_Pot = 500
            
    # No win
    else:
        print(Fruits + "\nPlease try again. \n")
    
    return Player_Money, Bet, Jack_Pot, win, Fruit_Reel

def main():
    """ The Main function that runs the game loop """
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 5
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    Fruit_Reel = ["spin.jpg","spin.jpg","spin.jpg"]
    #D - Display Config
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("U Got Died Slot Machine")

    #E - Entities (add slot machine template)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("slotMachineTemplate.jpg")
    #load the default image 
    slot1 = pygame.Surface((200, 200))
    slot1 = slot1.convert()
    slot1 = pygame.image.load("spin.jpg")
    slot2 = slot1
    slot3 = slot1
    #load the spin button
    buttonSpin = Buttons.Button()
    #load the text and labels
    myFont = pygame.font.SysFont("Arial", 28)
    creditText = myFont.render("" + str(Player_Money), 1, (255, 255, 0))
    lblCredit = myFont.render("Credit", 1, (255, 255, 0))
    betText = myFont.render("" + str(Bet), 1, (255, 255, 0))
    lblBet = myFont.render("Bet", 1, (255, 255, 0))
    jackPotText = myFont.render("" + str(Jack_Pot), 1, (255, 255, 0))
    lblJackpot = myFont.render("Jackpot", 1, (255, 255, 0))
    #load the JackPot!! message label
    jackpotMessage = myFont.render("", 1, (255, 255, 0))
    #load the reset and quit button
    buttonReset = Buttons.Button()
    buttonQuit = Buttons.Button()
    
    # Flag to initiate the game loop
    clock = pygame.time.Clock()
    KeepGoing = True
    
    while KeepGoing == True:
        #T - Timer to set frame rate
        clock.tick(30)
        win = 0
        
        #Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                KeepGoing = False
            #if the mouse is pressed down
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #if the mouse presses on reset
                if buttonReset.pressed(pygame.mouse.get_pos()):
                    #reset variables
                    Player_Money = 1000
                    Jack_Pot = 500
                    Turn = 1
                    Bet = 5
                    Prev_Bet=0
                    win_number = 0
                    loss_number = 0
                    Fruit_Reel = ["spin.jpg","spin.jpg","spin.jpg"]
                # if the mouse presses quit
                elif buttonQuit.pressed(pygame.mouse.get_pos()):
                    #exit the loop and the program
                    KeepGoing = False
                elif buttonSpin.pressed(pygame.mouse.get_pos()):
                    # User Input
                    #if Prompt == "" and Turn >1:
                        #Bet = Prev_Bet
                        #print("Using Previous Bet")
                    if Bet > Player_Money:
                        print("Sorry, you only have $" + str(Player_Money) + " \n")
                    elif Bet <= Player_Money:
                        Turn +=1
                        Prev_Bet = Bet
                        Player_Money, Bet, Jack_Pot, win, Fruit_Reel = pullthehandle(Player_Money, Bet, Jack_Pot, win, Fruit_Reel)
            
                elif is_number(Prompt ):
                    Bet = int(Prompt )
                #not enough money
                    if Bet > Player_Money:
                        print("Sorry, you only have $" + str(Player_Money) + " \n")

                # Spin the wheel
                elif Bet <= Player_Money:
                    Turn +=1
                    Prev_Bet = Bet
                    Player_Money, Bet, Jack_Pot, win, Fruit_Reel = pullthehandle(Player_Money, Bet, Jack_Pot, win, Fruit_Reel)
        #if jack pot has happened display JackPot on the screen
        if Jack_Pot == "500" and Turn > 0:
            jackpotMessage = myFont.render("JackPot!!!", 1, (255, 255, 0))
        #refresh the text boxes
        creditText = myFont.render("" + str(Player_Money), 1, (255, 255, 0))
        betText = myFont.render("" + str(Bet), 1, (255, 255, 0))
        jackpotText = myFont.render("" + str(Jack_Pot), 1, (255, 255, 0))  
        #change the slot images
        slot1 = pygame.image.load(Fruit_Reel[0]) 
        slot2 = pygame.image.load(Fruit_Reel[1])
        slot3 = pygame.image.load(Fruit_Reel[2]) 
         
        #R - Refresh display
        screen.blit(background, (0, 0))
        #display the slot default images
        screen.blit(slot1, (25, 30))
        screen.blit(slot2, (225, 30))
        screen.blit(slot3, (425, 30))
        #display the spin button
        buttonSpin.create_button(screen, (107,142,35), 460, 375, 150, 95, 0, "Spin", 
                                 (255,255,255))
        #display text fields and labels
        screen.blit(creditText, (90, 290))
        screen.blit(lblCredit, (80, 340))
        screen.blit(betText, (305, 290))
        screen.blit(lblBet, (290, 340))
        screen.blit(jackpotText,(400, 290))
        screen.blit(lblJackpot, (440, 340))
        screen.blit(jackpotMessage, (260, 230))
        #display the reset and quit button
        buttonReset.create_button(screen, (107,142,35), 10, 375, 200, 95, 0, "Reset", 
                                 (255,255,255))
        buttonQuit.create_button(screen, (107,142,35), 240, 375, 200, 95, 0, "Quit", 
                                 (255,255,255))
        pygame.display.flip()       

    #The End
    print("- Program Terminated -")
    
if __name__ == "__main__": main()