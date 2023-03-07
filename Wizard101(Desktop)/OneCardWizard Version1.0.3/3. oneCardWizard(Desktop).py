from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

print(f"""{time.asctime()}
Starting oneCardWizard.py, please wait...""")



# Returns a list: cardX, CardY, Cardwidth, cardHeight
def image_Coords(imageName):
    if pyautogui.locateOnScreen(imageName) == None:
        return False 
    else:
        card = str(pyautogui.locateOnScreen(imageName))
        
        card = card.replace('Box(left=', '')
        commaIndex = card.find(',')
        cardX = int(card[0:commaIndex])

        card = card.replace(f'{cardX}, top=','')
        commaIndex = card.find(',')
        cardY = int(card[0:commaIndex])

        card = card.replace(f'{cardY}, width=', '')
        commaIndex = card.find(',')
        cardWidth = int(card[0:commaIndex])

        card = card.replace(f'{cardWidth}, height=', '')
        cardHeight = int(card[0:-1])

        coords = []
        coords.append(cardX)
        coords.append(cardY)
        coords.append(cardWidth)
        coords.append(cardHeight)

        return(coords)


    
#Returns the center of an image in a list [x,y] 
def image_Center(imageName): 
    if pyautogui.locateOnScreen(imageName, confidence=0.8) == None:
        return False 
    else:
        card = str(pyautogui.locateOnScreen(imageName, confidence=0.8))

        card = card.replace('Box(left=', '')
        commaIndex = card.find(',')
        cardX = int(card[0:commaIndex])

        card = card.replace(f'{cardX}, top=','')
        commaIndex = card.find(',')
        cardY = int(card[0:commaIndex])

        card = card.replace(f'{cardY}, width=', '')
        commaIndex = card.find(',')
        cardWidth = int(card[0:commaIndex])

        card = card.replace(f'{cardWidth}, height=', '')
        cardHeight = int(card[0:-1])

        x_center = (cardX + (cardX + cardWidth))/2
        y_center = (cardY + (cardY + cardHeight))/2

        imageCenter = []

        imageCenter.append(x_center)
        imageCenter.append(y_center)

        return(imageCenter)

print("""

▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌

              One Card Wizard Pro (RTX3070 Desktop Version)
                             
▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌

""")



    
############################################################################################################################################################################################################
############################################################################################################################################################################################################
###                                                                                                                                                                                                      ###
###                                                                                    Required Variables Section                                                                                        ###
###                                                                                                                                                                                                      ###
############################################################################################################################################################################################################
############################################################################################################################################################################################################


   
# Format: imageX, imageY, imageWidth, imageHeight
# Use cardsCoordsWizard.py for coords
card1 = [721, 488, 67, 85] # Fill Me Out
card2 = [803, 486, 66, 104] # Fill Me Out
card3 = [883, 489, 69, 88] # Fill Me Out
card4 = [967, 489, 65, 85] # Fill Me Out
card5 = [1049, 487, 68, 84] # Fill Me Out
card6 = [1132, 486, 68, 107] # Fill Me Out
card7 = [1214, 486, 68, 88] # Fill Me Out

# Format: image.png
fleeImage = 'flee.png' 
passImage = 'pass.png'
noManaImage = 'nomana.png'
potionsImage = 'potions.png' 
fullBagImage = 'fullbag.png' 
quickSellImage = 'quicksell.png'
allImage = 'all.png'
noCrownsImage = 'nocrowns.png'
sellImage = 'sell.png'
sell2Image = 'sell2.png'
spellbookImage = 'spellbook.png' 
escMenuImage = 'escmenu.png' 

# Specific Cards
scarecrowImage = "scarecrow.png" 
#deathbladeImage = "deathblade.png"
#spiritbladImage = "spiritblade.png"

repeatingCard = scarecrowImage # Fill Me Out



############################################################################################################################################################################################################
############################################################################################################################################################################################################
###                                                                                                                                                                                                      ###
###                                                                                    End Of Section                                                                                                    ###
###                                                                                                                                                                                                      ###
############################################################################################################################################################################################################
############################################################################################################################################################################################################



def card_Center(card):
    centerX = (card[0] + (card[0] + card[2]))/2  
    centerY = (card[1] + (card[1] + card[3]))/2
    center = (centerX, centerY)
    return center



def click(x, y,):
          pyautogui.moveTo((x,y))
          time.sleep(0.1)
          pyautogui.leftClick((x,y))


# Work in progress         
def find_Enemy():
# X:  258 Y:   56 RGB: (187, 161, 112)
# X:  690 Y:   56 RGB: (187, 161, 112)
    enemies = 0
    if pyautogui.pixel(258, 56)[0] == 187:
        enemies =+ 1
    if pyautogui.pixel(690, 56)[0] == 187:
        enemies =+ 2
    return(enemies)



# Returns list of cards in your hand ex: [scarecrow, unavailable, scarecrow, ...]
def get_Hand_Cards():
    handCards = []
    for cycle in range(7):
        if pyautogui.locateOnScreen(repeatingCard, region=(sevenCards[cycle][0], sevenCards[cycle][1], sevenCards[cycle][2], sevenCards[cycle][3]), confidence=0.90) != None:
            handCards.append(repeatingCard)
            
        else:
            handCards.append("unavailable")
            
    return(handCards)

     
# Based of if the spellbook icon exists on your screen
def your_Turn():
    if pyautogui.locateOnScreen(spellbookImage) == None:
        return "yes"
    else:
        return "no"



sevenCards = [card1, card2, card3, card4, card5, card6, card7]

card1Center = card_Center(card1)
card2Center = card_Center(card2)
card3Center = card_Center(card3)
card4Center = card_Center(card4)
card5Center = card_Center(card5)
card6Center = card_Center(card6)
card7Center = card_Center(card7)
sevenCardsCenter = [card1Center, card2Center, card3Center, card4Center, card5Center, card6Center, card7Center]

potionsImageCenter = ''

quickSellImageCenter = ''
allImageCenter = ''
noCrownsImageCenter = ''
sellImageCenter = ''
sell2ImageCenter = ''

passImageCenter = ''


############################################################################################################################################################################################################
############################################################################################################################################################################################################
###                                                                                                                                                                                                      ###
###                                                                                    Action Begins                                                                                                     ###
###                                                                                                                                                                                                      ###
############################################################################################################################################################################################################
############################################################################################################################################################################################################



time.sleep(3) # Time to switch screens
print(f"""{time.asctime()}
Loop started

Rules:
1. HOLD 'q' to break
2. Keep cursor away from cards
3. Disable friend requests and notifications
4. SCRIPT WILL BREAK IF YOU HAVE LESS THAN 7 CARDS IN YOUR HAND
5. Only works with AOE spells 
""")

while True:
    
    if your_Turn() == "yes":

        
        if keyboard.is_pressed('q') == True:
            print(f"""{time.asctime()}
Breaking...
""") 
            break
        
        if pyautogui.locateOnScreen(escMenuImage, confidence=.9) != None:
            pyautogui.keyDown('b')
            time.sleep(0.1)
            pyautogui.keyUp('b')

        while True:
            if passImageCenter == "" or passImageCenter == False:
                passImageCenter = image_Center(passImage)
                
            else:
                break

        while True:        
            if keyboard.is_pressed('q') == True:
                print(f"""{time.asctime()}
Breaking...
""") 
                break
            
            elif pyautogui.locateOnScreen(fleeImage, confidence=.95) != None or pyautogui.locateOnScreen(spellbookImage, confidence=.9) != None:
                break
        
        pickCard = ""
        handCards = get_Hand_Cards()
        cardNumber = 0
        for card in handCards:
            if card == repeatingCard:
                pickCard = cardNumber
                break
            else:
                pass
            cardNumber = cardNumber + 1
            
        for i in range(7):
            if pickCard == i:
                click(sevenCardsCenter[i][0],sevenCardsCenter[i][1])
                click(passImageCenter[0], passImageCenter[1])

            else:
                pass
            
        click(passImageCenter[0], passImageCenter[1])

        if pyautogui.locateOnScreen(fleeImage, confidence=0.9) != None:
            while True:
                if pyautogui.locateOnScreen(fleeImage, confidence=0.9) == None:
                    break              

    elif your_Turn() == "no":
        if keyboard.is_pressed('q') == True:
            break
        pyautogui.keyDown("a")
        time.sleep(.01)
        pyautogui.keyUp("a")
        time.sleep(.01)
        if pyautogui.locateOnScreen(noManaImage, confidence=.95) != None:
            while True:
                if potionsImageCenter == '' or potionsImageCenter == False:
                    potionsImageCenter = image_Center(potionsImage)
                    print(f"""{time.asctime()}
Collecting {potionsImage} coordinates, this will only occur once.
""")
                else:
                    break
            click(potionsImageCenter[0], potionsImageCenter[1])
            print(f"""{time.asctime()}
Low mana, potion used.
""")        
            time.sleep(3)
        pyautogui.keyDown('b')
        time.sleep(0.1)
        pyautogui.keyUp('b')
        if pyautogui.locateOnScreen(fullBagImage, confidence=.95) != None:
            while True:
                if quickSellImageCenter == '' or quickSellImageCenter == False:
                    quickSellImageCenter = image_Center(quickSellImage)
                    print(f"""{time.asctime()}
Collecting {quickSellImage} coordinates, this will only occur once.
""")
                else:
                    break
            click(quickSellImageCenter[0], quickSellImageCenter[1])
            time.sleep(1)
            while True:
                if allImageCenter == '' or allImageCenter == False:
                    allImageCenter = image_Center(allImage)
                    print(f"""{time.asctime()}
Collecting {allImage} coordinates, this will only occur once.
""")
                else:
                    break
            click(allImageCenter[0], allImageCenter[1])
            time.sleep(0.5)
            while True:
                if noCrownsImageCenter == '' or noCrownsImageCenter == False:
                    noCrownsImageCenter = image_Center(noCrownsImage)
                    print(f"""{time.asctime()}
Collecting {noCrownsImage} coordinates, this will only occur once.
""")
                else:
                    break
            click(noCrownsImageCenter[0], noCrownsImageCenter[1])
            time.sleep(0.5)
            while True:
                if sellImageCenter == '' or sellImageCenter == False:
                    sellImageCenter = image_Center(sellImage)
                    print(f"""{time.asctime()}
Collecting {sellImage} coordinates, this will only occur once.
""")
                else:
                    break
            click(sellImageCenter[0], sellImageCenter[1])
            time.sleep(0.5)
            while True:
                if sell2ImageCenter == '' or sell2ImageCenter == False:
                    sell2ImageCenter = image_Center(sell2Image)
                    print(f"""{time.asctime()}
Collecting {sell2Image} coordinates, this will only occur once.
""")
                else:
                    break
            click(sell2ImageCenter[0], sell2ImageCenter[1])
            time.sleep(0.5)
            print(f"""{time.asctime()}
Bag Full, quick sold items.
""")
            time.sleep(3)



print(f"""{time.asctime()}
Closed oneCardWizard.py
""")




