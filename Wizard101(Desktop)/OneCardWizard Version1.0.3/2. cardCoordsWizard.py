from pyautogui import *
import pyautogui
import time



def image_Coords(imageName):
    if pyautogui.locateOnScreen(imageName, confidence =.7) == None:
        print(f"Can't find {imageName}")
        return False 
    else:
        card = str(pyautogui.locateOnScreen(imageName, confidence =0.7))
        
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



# Step 1: equip exactly 7 different cards in your deck
# Step 2: Get in a battle and take a screenshot when your cards appear.
# Step 3: Crop the cards out and make seven different images.
# Step 4: fill out the file name for the cards:
cardA = "thundersnake.png"
cardB = "frostbeetle.png"
cardC = "firecat.png"
cardD = "imp.png"
cardE = "scarecrow.png"
cardF = "scarab.png"
cardG = "darksprite.png"



# Step 5: Start another battle, and run the script when cards appear. Copy the output into other scripts.

CardA = image_Coords(cardA)
CardB = image_Coords(cardB)
CardC = image_Coords(cardC)
CardD = image_Coords(cardD)
CardE = image_Coords(cardE)
CardF = image_Coords(cardF)
CardG = image_Coords(cardG)


cardsAG = [CardA, CardB, CardC, CardD, CardE, CardF, CardG]
cardsAG = sorted(cardsAG, key=lambda l:l[0])

card1 = cardsAG[0]
card2 = cardsAG[1]
card3 = cardsAG[2]
card4 = cardsAG[3]
card5 = cardsAG[4]
card6 = cardsAG[5]
card7 = cardsAG[6]

print(f"""
card1 = {cardsAG[0]} # Fill Me Out
card2 = {cardsAG[1]} # Fill Me Out
card3 = {cardsAG[2]} # Fill Me Out
card4 = {cardsAG[3]} # Fill Me Out
card5 = {cardsAG[4]} # Fill Me Out
card6 = {cardsAG[5]} # Fill Me Out
card7 = {cardsAG[6]} # Fill Me Out
""")

# Copy the output to other .py files




                

