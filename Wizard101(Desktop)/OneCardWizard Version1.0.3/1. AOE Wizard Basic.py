from pyautogui import *
import pyautogui
import time
import keyboard

print(f"""{time.asctime()}

▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌

                                  AOE Card Wizard (Basic)
                             
▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌
""")



    
############################################################################################################################################################################################################
############################################################################################################################################################################################################
###                                                                                                                                                                                                      ###
###                                                                                    Required Variables Section                                                                                        ###
###                                                                                                                                                                                                      ###
############################################################################################################################################################################################################
############################################################################################################################################################################################################

pass_image = 'pass.png'
spellbookImage = 'spellbook.png' 
aoe_card = 'scarecrow.png'

############################################################################################################################################################################################################
############################################################################################################################################################################################################
###                                                                                                                                                                                                      ###
###                                                                                    End Of Section                                                                                                    ###
###                                                                                                                                                                                                      ###
############################################################################################################################################################################################################
############################################################################################################################################################################################################



def click(x, y,):
          pyautogui.moveTo((x,y))
          time.sleep(0.1)
          pyautogui.leftClick((x,y))



# Returns the center of an image in a list [x,y] 
def imageCenter(imageName): 
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


     
def your_Turn():
    if pyautogui.locateOnScreen(spellbookImage) == None:
        return "yes"
    else:
        return "no"



aoe_card_center = ''
pass_image_center = ''



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
2. Disable friend requests and notifications
""")



while True:
    if your_Turn() == "yes":        
        if keyboard.is_pressed('q') == True:
            print(f"""{time.asctime()}
Breaking...
""") 
            break

        while True:
            if keyboard.is_pressed('q') == True:
                print(f"""{time.asctime()}
Breaking...
""") 
                break
            if pass_image_center == "" or pass_image_center == False:
                pass_image_center = imageCenter(pass_image)
            else:
                break
            time.sleep(3)

        while True:        
            if keyboard.is_pressed('q') == True:
                print(f"""{time.asctime()}
Breaking...
""")    
                break
            
            if pyautogui.locateOnScreen(pass_image, confidence=.95) != None or pyautogui.locateOnScreen(spellbookImage, confidence=.9) != None:
                break


        if pyautogui.locateOnScreen(aoe_card, confidence = 0.9) != None:
            aoe_card_center = imageCenter(aoe_card)
            click(aoe_card_center[0], aoe_card_center[1])
            pyautogui.moveTo(pass_image_center[0] - pass_image_center[0], pass_image_center[1], 0.5)
        
        else:
            click(pass_image_center[0], pass_image_center[1])
            pyautogui.moveTo(pass_image_center[0] - pass_image_center[0], pass_image_center[1], 0.5)
        

    # Out Of Combat
    elif your_Turn() == "no":
        if keyboard.is_pressed('q') == True:
            break
        pyautogui.keyDown("a")
        time.sleep(.01)
        pyautogui.keyUp("a")
        time.sleep(.01)


# Closing Program
print(f"""{time.asctime()}
Closed oneCardWizard.py
""")




# Remove Cursor from pass button after clicing pass, same for aoe_card

