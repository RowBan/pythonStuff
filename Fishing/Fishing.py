import pyautogui as pg
import time
import keyboard

def main():
    pg.FAILSAFE = True
    countDownToStart()
    Fishing()
    
def countDownToStart():
    #Countdown timer
    print("Starting", end="")
    for i in range(0, 5):
        print(".")
        time.sleep(1)
    print("Started")   

def Fishing():
    while 1:
        if pg.locateOnScreen('fishingOff.png', region=(600, 900, 900, 1079), confidence=0.8):
            print("I can see it, starting to fish")
            time.sleep(0.3)
            keyboard.press_and_release('e')
            time.sleep(0.8)
        if pg.locateOnScreen('fishExclamation.png', confidence=0.8):
            print("Fish caught, pressing E")
            time.sleep(0.2)
            keyboard.press_and_release('e')
            time.sleep(0.2)
            
main()