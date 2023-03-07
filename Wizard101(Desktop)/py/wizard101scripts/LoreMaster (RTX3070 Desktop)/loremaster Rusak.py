import pyautogui
import time
import keyboard

print(f"""{time.asctime()}
Starting oneCardWizard.py, please wait...""")



def click(x,y):
    pyautogui.moveTo((x,y))
    time.sleep(0.1)
    pyautogui.leftClick()



def imageCoords(imageName):
# imageName must be a string.filetype
# Returns a list: cardX, CardY, Cardwidth, cardHeight
    if pyautogui.locateOnScreen(imageName, confidence=0.9) == None:
        return False 

    else:

        card = str(pyautogui.locateOnScreen(imageName, confidence=0.9))

    
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



def imageCenter(imageName):
#Returns the center of an image in a list [x,y] 


    if pyautogui.locateOnScreen(imageName, confidence=0.9) == None:
        return False 

    else:

        card = str(pyautogui.locateOnScreen(imageName, confidence=0.9))

    
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

                            Lore Master Farmer
                             
▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌▐░░░░░░░░░░░░░░░░▌

""")

############################################################################################################################################################################################################
############################################################################################################################################################################################################
###                                                                                                                                                                                                      ###
###                                                                                    Required Variables Section                                                                                        ###
###                                                                                                                                                                                                      ###
############################################################################################################################################################################################################
############################################################################################################################################################################################################


loadingScreenImage = 'loadingscreen.png'
spellbookImage = 'spellbook.png'
passImage = 'pass.png'
quitImage = 'quit.png'
playImage = 'play.png'

deathbladeImage = 'deathblade.png'
scarecrowImage = 'scarecrow.png'

player1 = [1531, 759]




############################################################################################################################################################################################################
############################################################################################################################################################################################################
###                                                                                                                                                                                                      ###
###                                                                                    End Of Section                                                                                                    ###
###                                                                                                                                                                                                      ###
############################################################################################################################################################################################################
############################################################################################################################################################################################################

def inCombat():
    if pyautogui.locateOnScreen(spellbookImage) != None:
        return "no"
    else:
        return "yes"


passImageCenter = ""
quitImageCenter = ""
playImageCenter = ""

deathbladeImageCenter = ""
scarecrowImageCenter = "" 
    
bossRoom = 0
step = 1

############################################################################################################################################################################################################
############################################################################################################################################################################################################
###                                                                                                                                                                                                      ###
###                                                                                    Action Begins                                                                                                     ###
###                                                                                                                                                                                                      ###
############################################################################################################################################################################################################
############################################################################################################################################################################################################

time.sleep(3)
print(f"""{time.asctime()}
Loop started

1. HOLD 'q' to break
""")


while True:
    if inCombat() == "no":

        if bossRoom == 0:
            time.sleep(5)
            print("not in combat")
                
            if keyboard.is_pressed('q') == True:
                print(f"""{time.asctime()}
    Breaking...
    """) 
                break

            pyautogui.keyDown("x")
            time.sleep(0.1)
            pyautogui.keyUp("x")

            while True:
                if pyautogui.locateOnScreen(loadingScreenImage, confidence=0.8) == None:  
                    print("waiting for loading screen")
                    
                else:
                    "loading screen loaded"
                    break

            while True:
                if pyautogui.locateOnScreen(loadingScreenImage, confidence=0.8) != None:
                    print("loading")
                    
                else:
                    "loading screen closed"
                    break
                
            print("I see lore master")
            time.sleep(4)
            pyautogui.leftClick(player1[0], player1[1])
            pyautogui.keyDown("w")
            time.sleep(6)
            

        elif bossRoom == 1:
            print("we are in the boss room, time to leave")
            pyautogui.keyDown("esc")
            time.sleep(0.1)
            pyautogui.keyUp("esc")

            while True:
                if quitImageCenter == "" or quitImageCenter == False: 
                    quitImageCenter = imageCenter(quitImage)
                    print(f" quit image = {quitImageCenter}")
                    
                else:
                    break
                
            click(quitImageCenter[0], quitImageCenter[1])

            while True:
                if playImageCenter == "" or playImageCenter == False:
                    playImageCenter = imageCenter(playImage)
                    print(f" play image = {playImageCenter}")
                    
                else:
                    break

            bossRoom = 0
                
            click(playImageCenter[0], playImageCenter[1])

            while True:
                if pyautogui.locateOnScreen(loadingScreenImage, confidence=0.8) == None:  
                    print("waiting for loading screen")
                    
                else:
                    "loading screen loaded"
                    break
            
            while True:
                if pyautogui.locateOnScreen(loadingScreenImage, confidence=0.8) != None:
                    print("loading")
                    
                else:
                    "loading screen closed"
                    break

                     
            
    elif inCombat() == "yes":
        print("in combat")
        bossRoom = 1
        pyautogui.keyUp("w")

        while True:
            if passImageCenter == ""  or passImageCenter == False:
                passImageCenter = imageCenter(passImage)
                print(passImageCenter)
            else:
                break
       
        if keyboard.is_pressed('q') == True:
            print(f"""{time.asctime()}
Breaking...
""") 
            break
  
                        
        while True:

            if pyautogui.locateOnScreen(deathbladeImage, confidence=0.9) != None and step == 1:
                deathbladeImageCenter = imageCenter(deathbladeImage)
                print(f" deathblade image center {deathbladeImageCenter}")
                click(deathbladeImageCenter[0], deathbladeImageCenter[1])
                click(player1[0], player1[1])
                step = 2
                
            elif pyautogui.locateOnScreen(scarecrowImage, confidence=0.9) != None and step == 2:
                scarecrowImageCenter = imageCenter(scarecrowImage)
                print(scarecrowImageCenter)
                click(scarecrowImageCenter[0], scarecrowImageCenter[1])
                pyautogui.moveTo(player1[0], player1[1])
                step = 1
                
            else:
                if pyautogui.locateOnScreen(passImage) != None:
                    click(passImageCenter[0], passImageCenter[1])
                    pyautogui.moveTo(player1[0], player1[1])

                elif pyautogui.locateOnScreen(spellbookImage) != None:
                    break

            print("looping")

        step = 1
        bossRoom = 1
                
            

        
        

        
        

        

    
        

    







































