import pyautogui
import time

def click(x,y):
    pyautogui.moveTo((x,y))
    time.sleep(0.1)
    pyautogui.leftClick()
    


def image_coords(imageName):
# imageName must be a string.filetype
# Returns a list: cardX, CardY, Cardwidth, cardHeight
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



def image_center(imageName):
#Returns the center of an image in a list [x,y] 


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

        x_center = (cardX + (cardX + cardWidth))/2
        y_center = (cardY + (cardY + cardHeight))/2

        imageCenter = []

        imageCenter.append(x_center)
        imageCenter.append(y_center)

        return(imageCenter)


#############################################################################################
#                                        Get Card                                           #
#############################################################################################



png = input("card file name: ")
if image_coords(png) != False:
    coords = image_coords(png)
    print(f"region=({coords[0]}, {coords[1]}, {coords[2]}, {coords[3]})")
    clickon = image_center(png)
    print(f"click({clickon[0]}, {clickon[1]})")
          
else:
    print("card not on screen")

