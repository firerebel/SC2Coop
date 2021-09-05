import pyautogui
from time import sleep
DELAY_BETWEEN_COMMANDS = 1.00

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")


initializePyAutoGUI()
countdownTimer()
while True:
    def main():
        #locateall()
        #levelonecommander()
        levelallcommander()
        killtheobelisk()

        if pyautogui.locateOnScreen('checklvl15.png', region=(629, 450, 20, 8)):
                #click ok
                pyautogui.click(639, 453, duration=0.25)


    #def locateall():
        #commander = list(pyautogui.locateAllOnScreen('testfind.png'))
        #if commander:
            #firstcmdr = commander[0]
            #click_point = pyautogui.center(firstcmdr)
            #pyautogui.click(click_point)
            #sleep(2)

    def levelonecommander():
        if pyautogui.locateOnScreen('checkready.png', region=(117, 628, 22, 12)):
            # click ok
            pyautogui.click(639, 453, duration=0.25)
            sleep(.5)
            pyautogui.moveTo(140, 634, 0.25)
            sleep(.5)
            # Click the ready button
            pyautogui.click()

    def levelallcommander():
        if pyautogui.locateOnScreen('checkready.png', region=(117, 628, 22, 12)):
            # click ok
            pyautogui.click(639, 453, duration=0.25)
            sleep(.5)
            pyautogui.click(473, 257, duration=0.25)
            sleep(.5)
            if not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(69, 161, 15, 2)):
                pyautogui.click(89, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(117, 161, 15, 2)):
                pyautogui.click(140, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(165, 161, 15, 2)):
                pyautogui.click(185, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(213, 161, 15, 2)):
                pyautogui.click(235, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(261, 161, 15, 2)):
                pyautogui.click(281, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(309, 161, 15, 2)):
                pyautogui.click(328, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(405, 161, 15, 2)):
                pyautogui.click(424, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(453, 161, 15, 2)):
                pyautogui.click(472, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(501, 161, 15, 2)):
                pyautogui.click(519, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(69, 230, 15, 2)):
                pyautogui.click(89, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(117, 230, 15, 2)):
                pyautogui.click(134, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(165, 230, 15, 2)):
                pyautogui.click(185, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(213, 230, 15, 2)):
                pyautogui.click(234, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(261, 230, 15, 2)):
                pyautogui.click(282, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(309, 230, 15, 2)):
                pyautogui.click(328, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(357, 230, 15, 2)):
                pyautogui.click(375, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(405, 230, 15, 2)):
                pyautogui.click(426, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
        elif pyautogui.locateOnScreen('checklvl15.png', region=(629, 450, 20, 8)):
            # click ok
            pyautogui.click(639, 453, duration=0.25)
            sleep(.5)
            pyautogui.click(473, 257, duration=0.25)
            sleep(.5)
            if not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(69, 161, 15, 2)):
                pyautogui.click(89, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(117, 161, 15, 2)):
                pyautogui.click(140, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(165, 161, 15, 2)):
                pyautogui.click(185, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(213, 161, 15, 2)):
                pyautogui.click(235, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(261, 161, 15, 2)):
                pyautogui.click(281, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(309, 161, 15, 2)):
                pyautogui.click(328, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(405, 161, 15, 2)):
                pyautogui.click(424, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(453, 161, 15, 2)):
                pyautogui.click(472, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(501, 161, 15, 2)):
                pyautogui.click(519, 189)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(69, 230, 15, 2)):
                pyautogui.click(89, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(117, 230, 15, 2)):
                pyautogui.click(134, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(165, 230, 15, 2)):
                pyautogui.click(185, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(213, 230, 15, 2)):
                pyautogui.click(234, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(261, 230, 15, 2)):
                pyautogui.click(282, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(309, 230, 15, 2)):
                pyautogui.click(328, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(357, 230, 15, 2)):
                pyautogui.click(375, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()
            elif not pyautogui.locateOnScreen('testfind.png', confidence=0.8, region=(405, 230, 15, 2)):
                pyautogui.click(426, 256)
                sleep(.5)
                pyautogui.moveTo(140, 634, 0.25)
                sleep(.5)
                # Click the ready button
                pyautogui.click()

    def killtheobelisk():
        if pyautogui.locateOnScreen('gamestarting.png', region=(430, 40, 58, 12)):
            sleep(38.00)
            # Select Units
            pyautogui.moveTo(1016, 54, 0.25)
            sleep(DELAY_BETWEEN_COMMANDS)
            pyautogui.dragTo(346, 507, button='left')
            sleep(DELAY_BETWEEN_COMMANDS)
            # minimap click
            pyautogui.click(98, 573, duration=0.25)
            # right click obelisk
            pyautogui.click(620, 325, duration=0.25, button='right')
            sleep(19)
            pyautogui.press('m')
            pyautogui.click(570, 275)
            pyautogui.press('m')
            pyautogui.click(570, 275)
            pyautogui.press('m')
            pyautogui.click(570, 275)
            sleep(2)
            # menu button
            pyautogui.click(1251, 541, duration=0.25)
            sleep(DELAY_BETWEEN_COMMANDS)
            # Quit button
            pyautogui.click(638, 340, duration=0.25)
            sleep(7)
            # Leave button
            pyautogui.click(155, 562, duration=0.25)

    if __name__ == "__main__":
        main()
