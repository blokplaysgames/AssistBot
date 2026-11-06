# Automatically assists an alliance member when attacking; locates and navigates to the
# assust flag and places skeletons on it. 

# THIS TOOL IS IN ALPHA, EXPECT BUGS.

# report any bugs you may find to blokplaysgames@gmail.com

# you can also report bugs to the github repo *link goes here once I make it*

print('AssistBot v0.0.1 now running, you have 10 seconds to tab back into your game before I take total control of your mouse. Any mouse movements may interfere with the macro.')
print('')
print('')


print('Automatically assists an alliance member when attacking; locates and navigates to the assist flag and places troops on it. THIS TOOL IS IN ALPHA, EXPECT BUGS. report any bugs you may find to blokplaysgames@gmail.com')
print('')
print("you can also report bugs to the github repo by selecting the Issues tab and creating a new issue. *link goes here once I make it*")
print('')
print('')
print('Questions? Comments? Concerns? Reach out at the email above, the repo should only be used for bugs')
print('')
print('')
print('This code was entirely written by one human, no genAI was used to make this code.')
print('')
print('')
print('')
print('                             KNOWN BUGS')
print('''
 - The macro can only move in one direction (0.0.2 will fix)
 - The macro only allows one troop type (will fix in beta v0.1.0)
 - The macro will only target one flag (no fix scheduled)
''')



import pyautogui as pagui # main macro library, used for kb+mouse control
# reminder: update docs to include opencv
from pyautogui import ImageNotFoundException # need this to run the try/except stuff
import time as t # I use this in literally every program I write, for obvious reasons
#t.sleep(10) # gives you time to tab back into the game window after running the program
pagui.FAILSAFE=True # move your mouse to the upper-left to kill the program instantly

screen_size_horiz,screen_size_vert=pagui.size()
 # I assume your screen won't change sizes while this code is running. If it does, too bad.

class begin_assist:
    while True:
        try:
            allianceChatCenter=pagui.locateCenterOnScreen('openAllianceChat.png')
            pagui.click('openAllianceChat.png') # open the  chat menu
            pagui.click('selectAssistScreen.png') # from the chat menu, select the assist tab
        except ImageNotFoundException:
            print('img not found, try again!') # type: ignore
            t.sleep(5) # lets you kill

    try:
        pagui.click('genericAssistButton.png') # this should only contain the button, not a name
    except ImageNotFoundException:
        pagui.click('genericAssistButton.png') # this should only contain the button, not a name

class locate_flags:
    global locate_directional_flag
    def locate_directional_flag():
        try:
            assist_flag_direction=pagui.locateCenterOnScreen('directionalAssistFlag.png')
        except ImageNotFoundException:
            print('The chosen user has not yet placed an assist flag')
            t.sleep(5)
            locate_directional_flag()
        if assist_flag_direction[1]<screen_size_vert/2 and assist_flag_direction[1]<screen_size_horiz/2:
            pagui.press('left') # actually do the math for this **** later, once i know my screen size
            # bug is known and will be fixed in 0.0.2
            locate_directional_flag() # yeah I'm nesting, sue me
        # repeat the above for the other 4 corners of the screen
        try:
            assist_flag_location=pagui.locateCenterOnScreen('assistFlagPreciseLocation')
            pagui.click('archers_overworld.png')
            pagui.click('assist_flag_location')
        except ImageNotFoundException:
            print('') # placeholder, will be fixed in 0.0.2


class assist_bot_run:
    begin_assist()
    locate_directional_flag()