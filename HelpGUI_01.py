from tkinter import * #import all of tkinter tools
from functools import partial #This prevents unwanted windows

import random

class Converter:#"Foo" and "bar" are just silly names  popularised by MIT about 1969
    def __init__(self, parent):
        #This is formatting variables
        background_color = "light blue"
        
        #Convert main screen GUI
        self.converter_frame = Frame(width=600, height=600, bg= background_color)
        self.converter_frame.grid()
        
        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "32", "bold"),
                                          bg= background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial","14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)
        
    def help(self):
        print("You asked for help!")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here!")
if __name__ == "__main__":
    root =Tk()# this means when we run root we will create a Tk window
    root.title( "Temperature Converter")
    # this line puts a header in the window 'paren' that we are opening
    something = Converter(root)
    #this line places the class Foo into the root window
    root.mainloop()
    #this run the application mainloop in root window

