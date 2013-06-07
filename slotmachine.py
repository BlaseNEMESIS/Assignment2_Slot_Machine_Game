# Source File Name: slotmachine.py
# Author's Name: Jonathan Hodder
# Last Modified By: Jonathan Hodder
# Date Last Modified: Monday June 3rd, 2013
#Program Description:  This program simulates a Slot Machine Game. It provides an GUI
#for the user.  The GUI contains 5 bet buttons where you can bet different values, a reset
#button that will reset the game, a spin button that lets you spin the wheel, also a quit 
#button to let you quit the game  


#Version: 0.1 - Original code provided from Teacher. 
#(Contains the framework for the slot machine)
#Version: 0.2 - Added pygame import and other pygame code from lesson 4.
#Version: 0.3 - Added default spin image and slot machine background.
#Version: 0.4 - Finished adding all the labels and buttons.  Still need to add functionality
# and figure out how to create text boxes in Pygame.
#Version: 0.5 - Removed Pygbutton and replaced it with buttons.py
#Completed jackpot message and have slot machine spin working.  
#Need to complete bet validation
#Version: 1.0 - Completed bet validation and completed coloring of buttons for different states 

#Used import Buttons.py
#Author: Simon H. Larsen
#Link: http://lagusan.com/button-drawer-python-2-6/
                
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
    #button color variables
    defaultBetButton = (255,0,0)
    disabledButton = (95,100,65)
    selectedBetButton = (0,255,0)
    defaultSpinButton = (107,142,35)
    #color variables
    bet5Color = selectedBetButton
    bet25Color = defaultBetButton
    bet50Color = defaultBetButton
    bet100Color = defaultBetButton
    bet250Color = defaultBetButton
    spinColor = defaultSpinButton
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
    messageText = myFont.render("", 1, (255, 255, 0))
    #load the reset and quit button
    buttonReset = Buttons.Button()
    buttonQuit = Buttons.Button()
    #load the bet buttons
    buttonBet5 = Buttons.Button()
    buttonBet25 = Buttons.Button()
    buttonBet50 = Buttons.Button()
    buttonBet100 = Buttons.Button()
    buttonBet250 = Buttons.Button()
    
    # Flag to initiate the game loop
    clock = pygame.time.Clock()
    KeepGoing = True
    
    while KeepGoing == True:
        #T - Timer to set frame rate
        clock.tick(30)
        win = 0
            
        #if statements to turn back on disabled buttons if you win enough money
        #to continue to use them again
        if Player_Money >= 25 and bet25Color == disabledButton:
            bet25Color = defaultBetButton
        if Player_Money >=50 and bet50Color == disabledButton:
            bet50Color = defaultBetButton
        if Player_Money >= 100 and bet100Color == disabledButton:
            bet100Color = defaultBetButton 
        if Player_Money >= 250 and bet250Color == disabledButton:
            bet250Color = defaultBetButton             
        #Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                KeepGoing = False
            #if the mouse is pressed down
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #if bet 5 is selected set bet to 5
                if buttonBet5.pressed(pygame.mouse.get_pos()):
                    messageText = myFont.render("", 1, (255, 255, 0))
                    #if you have enough money to bet with set the bet to 5
                    #change bet colors
                    if Player_Money >= 250:
                        bet250Color = defaultBetButton
                    if Player_Money >= 100:
                        bet100Color = defaultBetButton
                    if Player_Money >= 50:
                        bet50Color = defaultBetButton
                    if Player_Money >= 25:  
                        bet25Color = defaultBetButton 
                    if Player_Money >= 5: 
                        Bet = 5
                        bet5Color = selectedBetButton

                #if bet 25 is selected set bet to 25
                elif buttonBet25.pressed(pygame.mouse.get_pos()):
                    messageText = myFont.render("", 1, (255, 255, 0))
                    #if you have enough money to bet with set the bet to 25
                    #change bet colors
                    if Player_Money >= 250:
                        bet250Color = defaultBetButton
                    if Player_Money >= 100:
                        bet100Color = defaultBetButton
                    if Player_Money >= 50:
                        bet50Color = defaultBetButton
                    if Player_Money >= 25:    
                        Bet = 25
                        bet5Color = defaultBetButton
                        bet25Color = selectedBetButton
                    #send a message saying they do not have enough
                    else:
                        messageText = myFont.render("Do not have $25 to bet with", 1, (255, 255, 0))
                #if bet 50 is selected set bet to 50
                elif buttonBet50.pressed(pygame.mouse.get_pos()):
                    messageText = myFont.render("", 1, (255, 255, 0))
                    if Player_Money >= 250:
                        bet250Color = defaultBetButton
                    if Player_Money >= 100:
                        bet100Color = defaultBetButton
                    if Player_Money >= 50:    
                        Bet = 50
                        bet5Color = defaultBetButton
                        bet25Color = defaultBetButton
                        bet50Color = selectedBetButton
                    else:
                        messageText = myFont.render("Do not have $50 to bet with", 1, (255, 255, 0))
                #if bet 100 is selected set bet to 100
                elif buttonBet100.pressed(pygame.mouse.get_pos()):
                    messageText = myFont.render("", 1, (255, 255, 0))
                    #change bet colors
                    if Player_Money >= 250:
                        bet250Color = defaultBetButton
                    if Player_Money >= 100:    
                        Bet = 100
                        bet5Color = defaultBetButton
                        bet25Color = defaultBetButton
                        bet50Color = defaultBetButton
                        bet100Color = selectedBetButton    
                    else:
                        messageText = myFont.render("Do not have $100 to bet with", 1, (255, 255, 0))
                #if bet 250 is selected set bet to 250
                elif buttonBet250.pressed(pygame.mouse.get_pos()):
                    messageText = myFont.render("", 1, (255, 255, 0))
                    if Player_Money >= 250:    
                        Bet = 250
                        #change bet colors
                        bet5Color = defaultBetButton
                        bet25Color = defaultBetButton
                        bet50Color = defaultBetButton
                        bet100Color = defaultBetButton
                        bet250Color = selectedBetButton
                    else:
                        messageText = myFont.render("Do not have $250 to bet with", 1, (255, 255, 0))
                #if the mouse presses on reset
                elif buttonReset.pressed(pygame.mouse.get_pos()):
                    #reset variables
                    Player_Money = 1000
                    Jack_Pot = 500
                    Turn = 1
                    Bet = 5
                    Prev_Bet=0
                    win_number = 0
                    loss_number = 0
                    #reset slot images
                    Fruit_Reel = ["spin.jpg","spin.jpg","spin.jpg"]
                    #reset button colors
                    bet5Color = selectedBetButton
                    bet25Color = defaultBetButton
                    bet50Color = defaultBetButton
                    bet100Color = defaultBetButton
                    bet250Color = defaultBetButton
                    spinColor = defaultSpinButton
                    #Reset the message text
                    messageText = myFont.render("", 1, (255, 255, 0))
                # if the mouse presses quit
                elif buttonQuit.pressed(pygame.mouse.get_pos()):
                    #exit the loop and the program
                    KeepGoing = False
                elif buttonSpin.pressed(pygame.mouse.get_pos()):
                    messageText = myFont.render("", 1, (255, 255, 0))
                    if Player_Money >= Bet:
                        Turn +=1
                        Prev_Bet = Bet
                        Player_Money, Bet, Jack_Pot, win, Fruit_Reel = pullthehandle(Player_Money, Bet, Jack_Pot, win, Fruit_Reel)
                        #check if there is less than 250 left to bet
                    if Player_Money < 250:
                        bet250Color = disabledButton
                        bet = 100
                    #check if there is less than 100 left to bet
                    if Player_Money < 100:
                        bet100Color = disabledButton
                        bet = 50
                    #check if there is less than 50 left to bet
                    if Player_Money < 50:
                        bet50Color = disabledButton
                        bet = 25
                    #check if there is less than 25 left to bet
                    if Player_Money < 25:
                        bet25Color = disabledButton
                        bet = 5
                    #check if there is less than 5 left to bet
                    if Player_Money < 5:
                        bet5Color = disabledButton
                        spinColor = disabledButton
                        bet = 0
                        
        if Player_Money < 5: 
            messageText = myFont.render("You are out of money to bet with", 1, (255, 255, 0))
        #if jack pot has happened display JackPot on the screen
        elif Jack_Pot == "500" and Turn > 0:
            messageText = myFont.render("JackPot!!!", 1, (255, 255, 0))

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
        buttonSpin.create_button(screen, (spinColor), 490, 375, 150, 95, 0, "Spin", 
                                 (255,255,255))
        #display text fields and labels
        screen.blit(creditText, (90, 290))
        screen.blit(lblCredit, (80, 340))
        screen.blit(betText, (305, 290))
        screen.blit(lblBet, (290, 340))
        screen.blit(jackpotText,(400, 290))
        screen.blit(lblJackpot, (440, 340))
        screen.blit(messageText, (260, 230))
        #display the reset and quit button
        buttonReset.create_button(screen, (107,142,35), 10, 375, 150, 95, 0, "Reset", 
                                 (255,255,255))
        buttonQuit.create_button(screen, (107,142,35), 170, 375, 150, 95, 0, "Quit", 
                                 (255,255,255))
        #display the bet buttons
        buttonBet5.create_button(screen, (bet5Color), 330, 375, 50, 50, 0, "5  ", 
                                 (255,255,255))
        buttonBet25.create_button(screen, (bet25Color), 380, 375, 50, 50, 0, "25 ", 
                                 (255,255,255))
        buttonBet50.create_button(screen, (bet50Color), 330, 430, 50, 50, 0, "50 ", 
                                 (255,255,255))
        buttonBet100.create_button(screen, (bet100Color), 380, 430, 50, 50, 0, "100", 
                                 (255,255,255))
        buttonBet250.create_button(screen, (bet250Color), 435, 400, 50, 50, 0, "250", 
                                 (255,255,255))
        pygame.display.flip()       

    #The End
    print("- Program Terminated -")
    
if __name__ == "__main__": main()