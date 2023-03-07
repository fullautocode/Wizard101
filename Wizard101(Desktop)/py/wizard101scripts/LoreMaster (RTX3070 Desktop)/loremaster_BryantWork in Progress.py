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
scarecrowgImage = 'scarecrowg.png'
scarecrow1Image = 'scarecrow1.png'
epicImage = 'epic.png'

player1 = [3168, 2015]




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
scarecrow1ImageCenter = ""
scarecrowgImageCenter = ""
    
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
            bossRoom = 1
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
                    print(f" quit image = {quitImageCenter}")
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
    
        if keyboard.is_pressed("w") == True:
            pyautogui.keyUp("w")

        while True:
            if passImageCenter == ""  or False:
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
# Click Epic, Click Scare Crow
            #pyautogui.moveTo(player1[0], player1[1], 0.5)
        
            if pyautogui.locateOnScreen(epicImage, confidence=0.9) != None and pyautogui.locateOnScreen(scarecrowImage, confidence=0.9) != None and pyautogui.locateOnScreen(deathbladeImage, confidence=0.9) != None and step == 1:
                epicImageCenter = imageCenter(epicImage)
                print(f" epic image center {epicImageCenter}")
                click(epicImageCenter[0], epicImageCenter[1])
                pyautogui.moveTo(player1[0], player1[1], 0.5)
                scarecrow1ImageCenter = imageCenter(scarecrow1Image)
                print(scarecrow1ImageCenter)
                click(scarecrow1ImageCenter[0], scarecrow1ImageCenter[1])
                pyautogui.moveTo(player1[0], player1[1], 0.5)

                deathbladeImageCenter = imageCenter(deathbladeImage)
                print(f" deathblade image center {deathbladeImageCenter}")
                click(deathbladeImageCenter[0], deathbladeImageCenter[1])
                pyautogui.moveTo(player1[0], player1[1], 0.5)
                pyautogui.leftClick()   
                step = 2
                print(f"on step {step}")
                
            elif pyautogui.locateOnScreen(scarecrowgImage, confidence=0.8) != None and step == 2:
                x = pyautogui.locateOnScreen(scarecrowgImage, confidence=0.8)
                print(f"this is sacrecrowg image coords {x}")
                print(f"scarecrowg image is {scarecrowgImage}")
                time.sleep(1)
                scarecrowgImageCenter = imageCenter(scarecrowgImage)
                print(scarecrowgImageCenter)
                click(scarecrowgImageCenter[0], scarecrowgImageCenter[1])
                pyautogui.moveTo(player1[0], player1[1], 0.5)
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
                
            

        
        

        
        

        

    
        

    







































