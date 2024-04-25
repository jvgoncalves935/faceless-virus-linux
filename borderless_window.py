#Importing the tkinter library
from tkinter import *
import tkinter
import os
import sys
from PIL import Image, ImageTk
import threading
from playsound import playsound

win_nicole = Tk()
win_nicole_width = 0
win_nicole_height = 0
win_nicole_border_left = 0
win_nicole_border_right = 0
win_nicole_border_up = 0
win_nicole_border_down = 0
win_nicole_direction = 0

def start_music_thread():
    music_loop_thread = threading.Thread(target=music_loop, name='FACELESSGAMES.COM.BR_ACELERADO_BLZ')
    music_loop_thread.daemon = True # shut down music thread when the rest of the program exits
    music_loop_thread.start()

def start_nicole_mode():
    global win_nicole_direction
    global win_nicole_border_left
    global win_nicole_border_right
    global win_nicole_border_down
    global win_nicole_border_up
    global win_nicole_width
    global win_nicole_height
    
    calculate_borders_nicole_mode()

    #print(win_nicole_width,win_nicole_height)

    win_nicole.geometry('%dx%d+%d+%d' % (250, 250, 0, win_nicole_height-250))

    image = Image.open(get_path('nicolexd.png'))
    display = ImageTk.PhotoImage(image)

    lab= Label(win_nicole, image=display,bg='grey').pack(anchor=tkinter.SE)

    #Make the window borderless
    win_nicole.overrideredirect(True)

    #Create a transparent window
    win_nicole.wm_attributes("-transparentcolor", 'grey')
    win_nicole.attributes('-topmost',True)

    win_nicole.after(1,update_nicole_mode, 0, win_nicole_height-250)
    
    start_music_thread()

    win_nicole.mainloop()
    

def calculate_borders_nicole_mode():
    global win_nicole_direction
    global win_nicole_border_left
    global win_nicole_border_right
    global win_nicole_border_down
    global win_nicole_border_up
    global win_nicole_width
    global win_nicole_height

    win_nicole_width = win_nicole.winfo_screenwidth()
    win_nicole_height = win_nicole.winfo_screenheight()
    win_nicole_border_right = win_nicole_width - 235
    win_nicole_border_down = win_nicole_height - 250
    win_nicole_border_left = -18

def change_direction_nicole_mode(pos_x,pos_y):
    global win_nicole_direction
    global win_nicole_border_left
    global win_nicole_border_right
    global win_nicole_border_down
    global win_nicole_border_up

    #print(pos_x,pos_y,"modo:",win_nicole_direction)
    
    if(pos_x >= win_nicole_border_right and pos_y >= win_nicole_border_down):
        win_nicole_direction = 1
        calculate_borders_nicole_mode()
        return
    if(pos_x >= win_nicole_border_right and pos_y <= win_nicole_border_up):
        win_nicole_direction = 2
        calculate_borders_nicole_mode()
        return
    if(pos_x <= win_nicole_border_left and pos_y <= win_nicole_border_up):
        win_nicole_direction = 3
        calculate_borders_nicole_mode()
        return
    if(pos_x <= win_nicole_border_left and pos_y >= win_nicole_border_down):
        win_nicole_direction = 0
        calculate_borders_nicole_mode()
        return

def change_position_nicole_mode(pos_x,pos_y):
    if(win_nicole_direction == 0):
        return pos_x+6,pos_y
    if(win_nicole_direction == 1):
        return pos_x,pos_y-6
    if(win_nicole_direction == 2):
        return pos_x-6,pos_y
    if(win_nicole_direction == 3):
        return pos_x,pos_y+6
    

def update_nicole_mode(pos_x,pos_y):
    change_direction_nicole_mode(pos_x,pos_y)
    
    new_pos_x, new_pos_y = change_position_nicole_mode(pos_x,pos_y)

    win_nicole.geometry('%dx%d+%d+%d' % (250, 250, new_pos_x,new_pos_y))
    
    win_nicole.after(15,update_nicole_mode,new_pos_x, new_pos_y)

def music_loop():
    while True:
        playsound(get_path('FACELESSGAMES.COM.BR_ACELERADO_BLZ.mp3'), block=True)

def get_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    start_nicole_mode()

