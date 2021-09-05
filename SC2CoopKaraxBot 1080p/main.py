import pyautogui
from time import sleep
DELAY_BETWEEN_COMMANDS = 1.00

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = False


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

        tradeWithMerchant()
        killtheobelisk()

    def testfunction():
        pyautogui.click(163, 864, duration=0.25)
        sleep(10)


    def tradeWithMerchant():
                if pyautogui.locateOnScreen('checkready.png', confidence=0.8, region=(176, 943, 33, 16)):
                    # Move mouse to ready button
                    pyautogui.moveTo(221, 946, 0.25)
                    sleep(.5)
                    # Click the ready button
                    pyautogui.click()
    def killtheobelisk():
                if pyautogui.locateOnScreen('gamestarting.png', confidence=0.8, region=(649, 62, 58, 13)):
                    # Allow time for the game to load
                    sleep(35)
                    # Select Units
                    pyautogui.moveTo(271, 104, 0.25)
                    sleep(DELAY_BETWEEN_COMMANDS)
                    pyautogui.dragTo(1351, 784, button='left')
                    sleep(DELAY_BETWEEN_COMMANDS)
                    # minimap click
                    pyautogui.click(163, 864, duration=0.25)
                    # right click obelisk
                    pyautogui.click(1794, 291, duration=0.25, button='right')
                    sleep(14)
                    # click orbital strike
                    pyautogui.click(804, 44, duration=0.25)
                    # kill obelisk
                    pyautogui.click(1794, 291, duration=0.25)
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.45)
                    pyautogui.press('escape')
                    sleep(.1)
                    #move tank onto target
                    pyautogui.press('m')
                    pyautogui.click(1830, 261)
                    sleep(.1)
                    pyautogui.press('m')
                    pyautogui.click(1830, 261)
                    sleep(.1)
                    pyautogui.press('m')
                    pyautogui.click(1830, 261)
                    sleep(.1)
                    pyautogui.press('m')
                    pyautogui.click(1830, 261)
                    sleep(.1)
                    #select orbital strike
                    pyautogui.click(804, 44, duration=0.1)
                    sleep(.1)
                    #kill 2nd obelisk
                    pyautogui.click(126, 295, duration=0.1)
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(.15)
                    pyautogui.click()
                    sleep(3)
                    # menu button
                    pyautogui.click(1880, 814, duration=0.25)
                    sleep(DELAY_BETWEEN_COMMANDS)
                    # Quit button
                    pyautogui.click(960, 510, duration=0.25)
                    sleep(7)
                    # Leave button
                    pyautogui.click(225, 842, duration=0.25)


    if __name__ == "__main__":
        main()
