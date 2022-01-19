import pyautogui
import random
from time import time, sleep

# set variables
pyautogui.FAILSAFE= False

def findCenter():
    width, height= pyautogui.size()
    return (width/2, height/2)


while True:    
    moveTime = 30
    
    # move cursor every 30 sec 
    sleep(moveTime)

    centerCordinates = findCenter()
    pyautogui.moveTo(centerCordinates)
    
    # keeing the mouse click in fourth quadrant of screen
    clickWidth = random.randint(1500,1900) 
    clickHeight = random.randint(500,900)

    pyautogui.click(x=clickWidth,y=clickHeight)
    

    screenWidth, screenheight = pyautogui.size()
    newX = random.randint(0,screenWidth)
    newY = random.randint(0,screenheight)
    print('(x,y) : (',newX,',',newY,')')
    
    pyautogui.dragTo(newX,newY) #drag mouse to random number pixels
    
