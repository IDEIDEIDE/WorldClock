#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 09:19:37 2022

@author: clockshield
"""

from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root = Tk()
root.geometry("600x450")



india_label = Label(root, text = "India")
india_label.place(relx = 0.2, rely = 0.05, anchor = CENTER)
    
india_time = Label(root)
india_time.place(relx = 0.2, rely = 0.3, anchor = CENTER)


usa_label = Label(root, text = "USA")
usa_label.place(relx = 0.7, rely = 0.05, anchor = CENTER)

usa_time = Label(root)
usa_time.place(relx = 0.7, rely = 0.3, anchor = CENTER)


australia_label = Label(root, text = "Australia")
australia_label.place(relx = 0.2, rely = 0.7, anchor = CENTER)
    
australia_time = Label(root)
australia_time.place(relx = 0.2, rely = 0.8, anchor = CENTER)


japan_label = Label(root, text = "Japan")
japan_label.place(relx = 0.7, rely = 0.7, anchor = CENTER)

japan_time = Label(root)
japan_time.place(relx = 0.7, rely = 0.8, anchor = CENTER)

class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = "Time :" + current_time
        india_time.after(200,self.times)
class usa():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time["text"] = "Time :" + current_time
        usa_time.after(200,self.times)
        
class Australia():
    def times(self):
        home = pytz.timezone('Australia/ACT')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        australia_time["text"] = "Time :" + current_time
        australia_time.after(200,self.times)
class Japan():
    def times(self):
        home = pytz.timezone('Japan')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        japan_time["text"] = "Time :" + current_time
        japan_time.after(200,self.times)
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time["text"] = "Time :" + current_time
        usa_time.after(200,self.times)
        
        
        
        
obj_india = India()
obj_usa = usa()    
obj_australia = Australia()
obj_japan_test = Japan()     
india_button = Button(root, text = "Show Time", command = obj_india.times)
india_button.place(relx = 0.2, rely = 0.4, anchor = CENTER)


usa_button = Button(root, text = "Show Time", command = obj_usa.times)
usa_button.place(relx = 0.7, rely = 0.4, anchor = CENTER)

australia_button = Button(root, text = "Show Time", command = obj_australia.times)
australia_button.place(relx = 0.2, rely = 0.9, anchor = CENTER)


japan_button = Button(root, text = "Show Time", command = obj_japan_test.times)
japan_button.place(relx = 0.7, rely = 0.9, anchor = CENTER)
root.mainloop()