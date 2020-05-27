from tkinter import * #import all of tkinter tools
from functools import partial #This prevents unwanted windows
import random
class Converter:#"Foo" and "bar" are just silly names  popularised by MIT about 1969
    def __init__(self):
        #This is formatting variables
        background_color = "light blue"
        
        #in actual program this is blank and is populated with user calculations
        self.all_calc_list = ['0 degree C is -17.8 degrees F',
        '0 degrees C is 32 degrees F',
        '40 degrees C is 104 degrees F',
        '40 degrees C is 4.4 degrees F',
        '12 degrees C is 53.6 degrees F',
        '24 degrees C is 75.2 degrees F',
        '100 degrees C is 37.8 degrees F']
        #Continue from 15
        
        #Convert main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg= background_color, pady=10)
        self.converter_frame.grid()
        
        #Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg= background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)
        
        self.history_button = Button(self.converter_frame, text="History",
                                  font=("Arial","14"),
                                  padx=10, pady=10, command=self.history)
        self.history_button.grid(row=1)
        
    def history(self):
        print("You asked for history!")
        get_history = history(self)
        get_history.history_text.configure(text="History text goes here!")
class history:
    def __init__(self, partner):

        background="orange" #pale green

        #disable history button
        partner.history_button.config(state=DISABLED)

        #Sets up child window (ie: history box)
        self.history_box = Toplevel()

        #If users press x button for the history box, you cant access it again so this fixes it
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))
        #Set up GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        #Set up history heading (Row 0)
        self.how_heading = Label(self.history_frame, text="Calcuation History", 
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)
        #history Text (label, row 1)
        self.history_text = Label(self.history_frame, 
                                  text="Here are your most recent "
                                       "calcuations. Please use the"
                                       "export button to create a text "
                                       "file of all your calculations for" 
                                       "this session", wrap=250,
                                       font="arial 10 italic",
                                       justify=LEFT, width=40, bg=background, )
        self.history_text.grid(row=1)
        
        #History output goes here

        ##Dismiss button (row 2)
        #self.dismiss_btn = Button(self.history_frame, text="Dismiss", width=10, bg="white",
                                  #command=partial(self.close_history, partner))
        #self.dismiss_btn.grid(row=2, pady=10)
        
        #History output goes here.. (row 2)
        
        #Export / Dismiss buttons frame (row  3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)
        
        #Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                                              font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)
        
        #Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                                              font="Aria 12 bold", command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)
        
        
    def close_history(self, partner):
        #Put history button to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()
if __name__ == "__main__":
    root =Tk()# this means when we run root we will create a Tk window
    root.title( "Temperature Converter")
    # this line puts a header in the window 'paren' that we are opening
    something = Converter()
    #this line places the class Foo into the root window
    root.mainloop()
    #this run the application mainloop in root window