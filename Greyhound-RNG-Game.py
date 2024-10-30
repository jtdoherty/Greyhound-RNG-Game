#project 1 Authors: Sam OFlanagan, Jack Doherty, Darren Del Sordo
import random#import these for later use
import sys
wallet = 500
total = 0
wager = ''
result = ''
wager = ''
result = ''
cTries = 0
total = 0
Zwager = ''
Zresult = ''
zTries = 0
randum = 0
Gwager = ''
result = ''
gTries = 1
guessTry = 1
Gtries = 1
numberQ=0
#below we defined all the function and put them into a function that totaled them all together
def getCHwager():
    global wager
    print('Welcome to cho-han.')
    while wager == '':
      print('Chose your wager Cho (even) or Han (odd).')
      wager=input()
      if wager == 'Cho' or wager == 'Han':
        break
      else:
        print('Please enter a valid wager. Either Cho or Han.')
        wager = ''

def diceRoll():
    global total,result
    total = random.randint(1,12)
    if total % 2 == 0:
      result = 'Cho'
    elif total % 2 == 1:
      result = 'Han'

def chResults():
    print ('The dice total is:', total)
    if wager == result:
        print ("You win.")
        #this is where we can add the betting stuff
    else:
        print ('You lost.')
        #add the losing money stuff here
#chohan function
def choHan():
    getCHwager()
    diceRoll()
    chResults()

def zambaleswager():
    global Zwager
    print('Welcome to Zambales. ')
    while Zwager == '':
      print('The goal of the game is to match the dice. Type (.) to continue.')
      Zwager=input()
      if Zwager == '.':
        break
      else:
        print('Please enter the correct character (.).')
        Zwager = ''
       
def ZdiceRoll():
    global zTries, Zresult,die1, die2
    for i in range (1,6):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if die1 == die2:
            print ("The two dice rolled are:",die1, die2,"You won.")
            Zresult == 'Win'
            zTries = zTries + 1
            #so we can see how many tries it takes to win. If z tries is 1 or 2 they did it in the first two attempts if its greater they dont get their money
            break
        elif die1 != die2:
            print ('The dice do not match:',die1, die2,'.Rolling again.')
            zTries = zTries + 1
            #this is so we can so how many tries it takes to win
            Zresult == 'Lose'
#zammbales function
def zambales():
    zambaleswager()
    ZdiceRoll()

def getGwager():
    global Gwager
    print('Welcome to number guesser.')
    while Gwager == '':
      print('Chose a number between 1 and 100.')
      Gwager=int(input())
      if Gwager <= 100 and Gwager >0:
        break
      else:
        print('Please enter a valid number between 1 and 100.')
        Gwager = ''
       
def randNum():
    global gTries, Gwager
    randnum = random.randint(1,100)
    if randnum == Gwager:
        numberQ = '1'
        print ('You won.')
        gTries = gTries +1
        sys.exit
    elif randnum != Gwager:
        print ('You lost.The number was:', randnum)
        gTries = gTries +1
        Gwager = ''
        numberQ= 2
       
#number guess funtion
def NumberGuess():
    global Gtries
    while Gtries <4:
        getGwager()
        randNum()
        Gtries = Gtries + 1
#this is the main menu. the user is brought back to this screen after ever game and their balance changes.
def mainmenu():
   global wallet
   while wallet > 0:  
        print("You have", wallet, "dollars in your wallet.")  
        bet = int(input("How much would you like to wager? "))    
        if bet > wallet:    
            print("You don't have that much money in your wallet.")
            continue    
        print("Choose the game you you would like to play.")  
        print("1. ChoHan")
        print("2. Zambales")
        print("3. Number Guessing")
        print("4. Quit")
        gamechoice = int(input("Welcome to the Greyhound Casino. Please pick the game you would like to play."))    
        if gamechoice == 1:
            choHan()
            if wager == result:
                wallet = (bet *2)+ wallet
            else:
                wallet = wallet - bet
        elif gamechoice == 2:  
            zambales()    
            global die1, die2,zTries
            if die1==die2 and zTries<3:
                wallet = (bet*2) + wallet
            elif die1==die2 and zTries<=5 and zTries>3:
                wallet = (bet*0) + wallet
            else:
                wallet = wallet - bet
        elif gamechoice == 3:  
            NumberGuess()    
            global numberQ, Gwager,gTries
            if numberQ == 1 and gTries <2:
                wallet = (bet *3)+wallet
            elif numberQ == 1 and gTries <3:
                wallet = (bet *2)+wallet
            elif numberQ == 1 and gTries <4:
                wallet = (bet *1)+wallet
            else:
                wallet = wallet - bet
        elif gamechoice == 4:
            print ('Thanks for playing good bye.')
            wallet = wallet - 10000000
            break
        else:  
            print("That choice is not valid. Please try again.")
            print("You have", wallet, "in your wallet Come again to O'Flanagan's casino!")  

 #this starts the code      
while wallet >0:
    mainmenu()
#this ends the code
if wallet <=0:
    print ('Your all out of money.Thanks for playing at the Greyhound Casino.')

