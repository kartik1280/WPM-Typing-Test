import curses 
from curses import wrapper
import time
from wonderwords import RandomSentence

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome To The Speed Typing Test!!") 
    stdscr.addstr("\npress any key to continue") 
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target) 
    stdscr.addstr(1,0,f"WPM:{wpm}") 

    for i,char in enumerate(current): #enumerate basically gives the index number (i) and the elements aswell (char)
        correct_char = target[i] #to see if the character in the list matches the sample text character's index
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0,i, char, color)


def wpm_test(stdscr, target_text):
    current_text = []  
    wpm = 0 
    start_time = time.time() #this code basically gives the current time at the particular instance 
    stdscr.nodelay(True) #this makes it so that our code doesnt stop when waiting for user to enter a key, however this will cause an exception with getkey()

    while True:
        time_elapsed = max(time.time() - start_time,1) #max(  ,1) to avoid zerodivison error
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5) #we are dividing the characters per minute and divinding it by 5 assuming the lenght of an average work is 5 which gives us wpm

        stdscr.clear()
        display_text(stdscr, target_text, current_text,wpm)
        stdscr.refresh()

        if "".join(current_text) == (target_text):
            stdscr.nodelay(False)
            break
        #"".join(current_text) converts list into string by taking all the characters and combines them together with "" as a seperator

        try:
            key = stdscr.getkey() #this is a blocking call basically it stops everything until the user types something
        except:
            continue

        if ord(key) == 27: #ordinal value is a numeric number given to keys on keyboards 27 in this case is escape if you press it you will exity the loop
            break
        if key in ("KEY_BACKSPACE",'\b','\x7f'): #if we hit backspace we get rid of the last item in the list so we used .pop and we have to do this manually because we are using curses where backspace doesnt work the same
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text): #this makes sure we dont write more character than the target text to avoid crashes
            current_text.append(key)

        stdscr.clear()
        stdscr.addstr(target_text) 

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()



def main(stdscr): 
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    s = RandomSentence()
    while True:
        target_text = s.sentence()
        wpm_test(stdscr, target_text)
        stdscr.addstr(2,0, "You Completed the Text! Press any key to coninue")
        stdscr.addstr(3,0, "To exit press escape.")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)
