import pyautogui as kb
import time

kb.FAILSAFE=False
counter = 5

# Open search and look for windows security
kb.press('winleft')
kb.write('windows security')
time.sleep(1)
kb.press('enter', presses=2, interval=1)

# Full Screen
kb.hotkey('winleft', 'up')

# Navigate to turn off Tampering protection
kb.press('tab', presses=4, interval=0.5)
kb.press('enter')
kb.press('tab', presses=4, interval=0.5)
kb.hotkey('shiftleft', 'space')

# A second wait needed as if you do it automatically then there is the
# possibility to have inaccuracy as there is another option inserted once tampering is turned off
time.sleep(1)

# Navigate to turn off realtime protection
while counter > 0:
    kb.hotkey('shiftleft', 'tab')
    counter = counter - 1
kb.hotkey('shiftleft', 'space')
