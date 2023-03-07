import pyautogui
import time


conf = 0.77
# Time sleep between arrows
x = .30

# Time between entering arrows
y = .05


while True:
    pyautogui.moveTo(1090, 744, .02)
    time.sleep(.01)
    pyautogui.leftClick()
    time.sleep(0.01)
    pyautogui.moveTo(1238, 858, .02)
    time.sleep(.01)
    pyautogui.leftClick()


    while True:
        if pyautogui.locateOnScreen('noarrow.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            print("Starting")
            break
        else:
            print("Waiting for game...")



    #Round 1
    while True:
        if pyautogui.locateOnScreen('noarrow.png', region=(906, 960, 100, 100), grayscale=True, confidence=0.9) == None:
            print("First Arrow Now")
            break
        else:
            print("Waiting for first arrow...")



    while True:
        
        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing1.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing2.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing3.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "right"

        break

    print(f"{one} {two} {three}")

    time.sleep(.5)

    pyautogui.keyDown(one)
    time.sleep(y)
    pyautogui.keyUp(one)
    time.sleep(y)
    pyautogui.keyDown(two)
    time.sleep(y)
    pyautogui.keyUp(two)
    time.sleep(y)
    pyautogui.keyDown(three)
    time.sleep(y)
    pyautogui.keyUp(three)
    time.sleep(1)

    # Round 2
    while True:
        if pyautogui.locateOnScreen('noarrow.png', region=(906, 960, 100, 100), grayscale=True, confidence=0.9) == None:
            print("First Arrow Now")
            break
        else:
            print("Waiting for first arrow...")


    while True:

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing1.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing2.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing3.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing4.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "right"

        break

    print(f"{one} {two} {three} {four}")

    time.sleep(.5)

    pyautogui.keyDown(one)
    time.sleep(y)
    pyautogui.keyUp(one)
    time.sleep(y)
    pyautogui.keyDown(two)
    time.sleep(y)
    pyautogui.keyUp(two)
    time.sleep(y)
    pyautogui.keyDown(three)
    time.sleep(y)
    pyautogui.keyUp(three)
    time.sleep(y)
    pyautogui.keyDown(four)
    time.sleep(y)
    pyautogui.keyUp(four)
    time.sleep(1)

    #Round 3

    while True:
        if pyautogui.locateOnScreen('noarrow.png', region=(906, 960, 100, 100), grayscale=True, confidence=0.9) == None:
            print("First Arrow Now")
            break
        else:
            print("Waiting for first arrow...")

    while True:

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing1.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing2.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing3.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing4.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing5.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "right"

        break


    print(f"{one} {two} {three} {four} {five}")

    time.sleep(.5)

    pyautogui.keyDown(one)
    time.sleep(y)
    pyautogui.keyUp(one)
    time.sleep(y)
    pyautogui.keyDown(two)
    time.sleep(y)
    pyautogui.keyUp(two)
    time.sleep(y)
    pyautogui.keyDown(three)
    time.sleep(y)
    pyautogui.keyUp(three)
    time.sleep(y)
    pyautogui.keyDown(four)
    time.sleep(y)
    pyautogui.keyUp(four)
    time.sleep(y)
    pyautogui.keyDown(five)
    time.sleep(y)
    pyautogui.keyUp(five)
    time.sleep(1)

    # Round 4

    while True:
        if pyautogui.locateOnScreen('noarrow.png', region=(906, 960, 100, 100), grayscale=True, confidence=0.9) == None:
            print("First Arrow Now")
            break
        else:
            print("Waiting for first arrow...")

    while True:

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing1.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing2.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "right"

        time.sleep(x)


        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing3.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing4.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing5.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing6.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            six = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            six = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            six = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            six = "right"

        break

    print(f"{one} {two} {three} {four} {five} {six}")

    time.sleep(.5)

    pyautogui.keyDown(one)
    time.sleep(y)
    pyautogui.keyUp(one)
    time.sleep(y)
    pyautogui.keyDown(two)
    time.sleep(y)
    pyautogui.keyUp(two)
    time.sleep(y)
    pyautogui.keyDown(three)
    time.sleep(y)
    pyautogui.keyUp(three)
    time.sleep(y)
    pyautogui.keyDown(four)
    time.sleep(y)
    pyautogui.keyUp(four)
    time.sleep(y)
    pyautogui.keyDown(five)
    time.sleep(y)
    pyautogui.keyUp(five)
    time.sleep(y)
    pyautogui.keyDown(six)
    time.sleep(y)
    pyautogui.keyUp(six)
    time.sleep(1)

    # round 5

    while True:
        if pyautogui.locateOnScreen('noarrow.png', region=(906, 960, 100, 100), grayscale=True, confidence=0.9) == None:
            print("First Arrow Now")
            break
        else:
            print("Waiting for first arrow...")

    while True:

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing1.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            one = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing2.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            two = "right"

        time.sleep(x)


        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing3.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            three = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing4.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            four = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing5.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            five = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing6.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            six = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            six = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            six = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            six = "right"

        time.sleep(x)

        iml = pyautogui.screenshot(region=(906, 960, 100, 100))
        iml.save(r"C:\Users\FullAutoDesktop\Desktop\DanceWizard\testing7.png")

        if pyautogui.locateOnScreen('up.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            seven = "up"

        if pyautogui.locateOnScreen('down.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            seven = "down"
            
        if pyautogui.locateOnScreen('left.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            seven = "left"

        if pyautogui.locateOnScreen('right.png', region=(906, 960, 100, 100), grayscale=True, confidence=conf) != None:
            seven = "right"

        break

    print(f"{one} {two} {three} {four} {five} {six} {seven}")

    time.sleep(.5)

    pyautogui.keyDown(one)
    time.sleep(y)
    pyautogui.keyUp(one)
    time.sleep(y)
    pyautogui.keyDown(two)
    time.sleep(y)
    pyautogui.keyUp(two)
    time.sleep(y)
    pyautogui.keyDown(three)
    time.sleep(y)
    pyautogui.keyUp(three)
    time.sleep(y)
    pyautogui.keyDown(four)
    time.sleep(y)
    pyautogui.keyUp(four)
    time.sleep(y)
    pyautogui.keyDown(five)
    time.sleep(y)
    pyautogui.keyUp(five)
    time.sleep(y)
    pyautogui.keyDown(six)
    time.sleep(y)
    pyautogui.keyUp(six)
    time.sleep(y)
    pyautogui.keyDown(seven)
    time.sleep(y)
    pyautogui.keyUp(seven)

    time.sleep(2)
    pyautogui.moveTo(1240, 859, 0.02)
    time.sleep(0.01)
    pyautogui.leftClick()
    time.sleep(0.01)
    pyautogui.moveTo(678, 751, 0.02)
    time.sleep(0.01)
    pyautogui.leftClick()
    time.sleep(0.01)
    pyautogui.moveTo(1240, 859, 0.02)
    time.sleep(0.01)
    pyautogui.leftClick()
    time.sleep(0.01)
    pyautogui.moveTo(953, 854, 0.1)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(5)

