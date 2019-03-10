#!/usr/bin/python3
# Version 1 (21/08/2018)
#CalculatorGUI.py Code written by Harry Brenton - (www.raspibotics.wixsite.com/blog) for support 

# Import tkinter library
from tkinter import *
from tkinter import messagebox
import math
# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify

    def __init__(self, master=None):
        # Parameters that you want to send through the Frame class.
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        

    def init_window(self):
        self.focus_set()
        # Set Window Size
        self.master.geometry("315x457")
        # Force Window Size / Disable Maximise
        self.master.resizable(0,0)
        # Set window title
        self.master.title("CalculatorGUI")
       
        # Pack all widgets into window
        self.pack(fill=BOTH, expand=1)

        # Setup operation variable
        operation = ""
        self.operation = operation
        operation2 = ""
        self.operation2 = operation2
        memory = - 0
        self.memory = memory
        
        # Setup number variables
        num1 = 0
        self.num1 = num1
        num3 = 0
        self.num3 = num3
        
        # SETUP WIDGETS

        message = lambda : messagebox.showinfo(title="About", message="A GUI Calculator coded in Python 3 by Harry Brenton")
        message2 = lambda : messagebox.showinfo(title="Help", message="Go to: www.raspibotics.wixsite.com/blog")

        menubar = Menu(self)
        menubar.add_command(label="About", command=message) # About - menu
        menubar.add_command(label="Help", command=message2)

        # display the menu
        root.config(menu=menubar)
        
        # Configure Display widget
        display = Entry(self, font=("Helvetica",36,"normal"), width=11)
        display.configure(bg="white",fg="grey", relief="flat", state="readonly")
        self.display = display

                
        # Configure button_1 widget (7)
        button_1 = Button(self, text="7", width=4, height=1,
                          command=self.button_1_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_1.configure(fg="white", relief="flat")
        self.button_1 = button_1

        # Configure button_2 widget (8)
        button_2 = Button(self, text="8", width=4, height=1,
                          command=self.button_2_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        
        button_2.configure(fg="white", relief="flat")
        self.button_2 = button_2

        # Configure button_3 widget (9)
        button_3 = Button(self, text="9", width=4, height=1,
                          command=self.button_3_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_3.configure(fg="white", relief="flat")
        self.button_3 = button_3

        # Configure button_ADD widget 
        button_ADD = Button(self, text="+", width=4, height=1,
                          command=self.button_ADD_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_ADD.configure(fg="white", relief="flat")
        self.button_ADD = button_ADD

        # Configure button_PERC widget 
        button_PERC = Button(self, text="%", width=4, height=1,             
                          command=self.button_PERC_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_PERC.configure(fg="white", relief="flat")
        self.button_PERC = button_PERC

        # Configure button_SQUARE widget 
        button_SQUARE = Button(self, text="x²", width=4, height=1,             #√
                          command=self.button_SQUARE_handler, bg="darkgrey",
                          font=("Helvetica",20,"bold"))
        button_SQUARE.configure(fg="white", relief="flat")
        self.button_SQUARE = button_SQUARE

         # Configure button_ROOT widget 
        button_ROOT = Button(self, text="√", width=4, height=1,
                          command=self.button_ROOT_handler, bg="darkgrey",
                          font=("Helvetica",20,"bold"))
        button_ROOT.configure(fg="white", relief="flat")
        self.button_ROOT = button_ROOT

         # Configure button_pi widget 
        button_pi = Button(self, text="π", width=4, height=1,
                          command=self.button_pi_handler, bg="darkgrey",
                          font=("Helvetica",20,"bold"))
        button_pi.configure(fg="white", relief="flat")
        self.button_pi = button_pi


        # Configure button_4 widget
        button_4 = Button(self, text="4", width=4, height=1,
                          command=self.button_4_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_4.configure(fg="white", relief="flat")
        self.button_4 = button_4

        # Configure button_5 widget (5)
        button_5 = Button(self, text="5", width=4, height=1,
                          command=self.button_5_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_5.configure(fg="white", relief="flat")
        self.button_5 = button_5

        # Configure button_6 widget (6)
        button_6 = Button(self, text="6", width=4, height=1,
                          command=self.button_6_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_6.configure(fg="white", relief="flat")
        self.button_6 = button_6

        # Configure button_SUB widget
        button_SUB = Button(self, text="-", width=4, height=1,
                          command=self.button_SUB_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_SUB.configure(fg="white", relief="flat")
        self.button_SUB = button_SUB

        # Configure button_7 widget (1)
        button_7 = Button(self, text="1", width=4, height=1,
                          command=self.button_7_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_7.configure(fg="white", relief="flat")
        self.button_7 = button_7

        # Configure button_8 widget (8)
        button_8 = Button(self, text="2", width=4, height=1,
                          command=self.button_8_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_8.configure(fg="white", relief="flat")
        self.button_8 = button_8

        # Configure button_9 widget (3)
        button_9 = Button(self, text="3", width=4, height=1,
                          command=self.button_9_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_9.configure(fg="white", relief="flat")
        self.button_9 = button_9

        # Configure button_MUL widget
        button_MUL = Button(self, text="x", width=4, height=1,
                          command=self.button_MUL_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_MUL.configure(fg="white", relief="flat")
        self.button_MUL = button_MUL

        # Configure button_10 widget (0)
        button_10 = Button(self, text="0", width=4, height=1,
                          command=self.button_10_handler, bg="lightgrey",
                          font=("Helvetica",20,"bold"))
        button_10.configure(fg="white", relief="flat")
        self.button_10 = button_10 

        # Configure button_11 widget (.)
        button_11 = Button(self, text=".", width=4, height=1,
                          command=self.button_11_handler, bg="darkgrey",
                          font=("Helvetica",20,"bold"))
        button_11.configure(fg="white", relief="flat")
        self.button_11 = button_11

        # Configure button_12 widget (C)
        button_12 = Button(self, text="CE", width=4, height=1,
                          command=self.button_12_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_12.configure(fg="white", relief="flat")
        self.button_12 = button_12

        # Configure button_DIV widget
        button_DIV = Button(self, text="÷", width=4, height=1,
                          command=self.button_DIV_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_DIV.configure(fg="white", relief="flat")
        self.button_DIV = button_DIV

        # Configure button_EQUALS widget
        button_EQUALS = Button(self, text="=", width=18, height=1,
                          command=self.button_EQUALS_handler, bg="grey",
                          font=("Helvetica",20,"bold"))
        button_EQUALS.configure(fg="white", relief="flat")
        self.button_EQUALS = button_EQUALS

        # Configure button_M+ widget (writes value to self.memory by additon of on display value)
        button_MPLUS = Button(self, text="M+", width=4, height=1,
                          command=self.button_MPLUS_handler, bg="darkorange",
                          font=("Helvetica",20,"bold"))
        button_MPLUS.configure(fg="white", relief="flat")
        self.button_MPLUS = button_MPLUS

          # Configure button_MR widget (reads self.memory)
        button_MREAD = Button(self, text="MR", width=4, height=1,
                          command=self.button_MREAD_handler, bg="darkorange",
                          font=("Helvetica",20,"bold"))
        button_MREAD.configure(fg="white", relief="flat")
        self.button_MREAD = button_MREAD

        # Configure button_M- widget (writes value to self.memory by subtraction of on display value)
        button_MSUB = Button(self, text="M-", width=4, height=1,
                          command=self.button_MSUB_handler, bg="darkorange",
                          font=("Helvetica",20,"bold"))
        button_MSUB.configure(fg="white", relief="flat")
        self.button_MSUB = button_MSUB

          # Configure button_MC widget (clears self.memory)
        button_MCLEAR = Button(self, text="MC", width=4, height=1,
                          command=self.button_MCLEAR_handler, bg="darkorange",
                          font=("Helvetica",20,"bold"))
        button_MCLEAR.configure(fg="white", relief="flat")
        self.button_MREAD = button_MCLEAR



        # Position Widgets
        display.place(x=0, y=0)
        button_1.place(x=0, y=173)#7
        button_2.place(x=79, y=173) #8
        button_3.place(x=158, y=173) #9
        button_ADD.place(x=237, y=287)#+
        button_4.place(x=0, y=230)#4
        button_5.place(x=79, y=230)#5
        button_6.place(x=158, y=230)#6
        button_SUB.place(x=237, y=230)#-
        button_7.place(x=0, y=287)#1
        button_8.place(x=79, y=287)#2
        button_9.place(x=158, y=287)#3
        button_MUL.place(x=237, y=173)#x
        button_10.place(x=79, y=344)#0
        button_11.place(x=0, y=344)#.
        button_12.place(x=0, y=116)#c
        button_DIV.place(x=237, y=116)#/
        button_EQUALS.place(x=0, y=401)#=
        button_PERC.place(x=237, y=344)#%
        button_SQUARE.place(x=79, y=116)
        button_ROOT.place(x=158, y=116)
        button_pi.place(x=158, y=344)#pi
        button_MPLUS.place(x=158 , y=59)
        button_MREAD.place(x=79 , y=59)
        button_MSUB.place(x=237 , y=59)
        button_MCLEAR.place(x=0 , y=59)


# EVENT HANDLERS

    def button_1_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "7")
        self.display.configure(state="readonly")
    def button_2_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "8")
        self.display.configure(state="readonly")
    def button_3_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "9")
        self.display.configure(state="readonly")
    def button_4_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "4")
        self.display.configure(state="readonly")
    def button_5_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "5")
        self.display.configure(state="readonly")
    def button_6_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "6")
        self.display.configure(state="readonly")
    def button_7_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "1")
        self.display.configure(state="readonly")
    def button_8_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "2")
        self.display.configure(state="readonly")
    def button_9_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "3")
        self.display.configure(state="readonly")
    def button_10_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "0")
        self.display.configure(state="readonly")
    def button_11_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", ".")
        self.display.configure(state="readonly")
    def button_12_handler(self):
        self.focus_set()
        self.display.configure(state="normal")
        self.display.delete(0,"end")
        self.num1 = 0
        self.num2 = 0
        self.operation = ""
        self.operation2 = ""
        self.display.configure(state="readonly")
    def button_pi_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", "3.141592653")
        self.display.configure(state="readonly")


    def button_MPLUS_handler(self):
        self.display.configure(state="normal")
        value = self.display.get()
        value = float(value)
        self.memory = value + self.memory
        self.display.configure(state="readonly")

    def button_MSUB_handler(self):
        self.display.configure(state="normal")
        value = self.display.get()
        value = float(value)
        self.memory = self.memory - value
        self.display.configure(state="readonly")


    def button_MREAD_handler(self):
        self.display.configure(state="normal")
        self.display.insert("end", self.memory)
        self.display.configure(state="readonly")

    def button_MCLEAR_handler(self):
        self.display.configure(state="normal")
        self.memory = 0
        self.display.insert("end", self.memory)
        self.display.configure(state="readonly")
        



    def button_ADD_handler(self):
        self.display.configure(state="normal")
        # Sets the operation variable to the relevant choice - used in the EQUALS_HANDLER() 
        self.operation = "+"
        # Gets user input from display
        self.num1 = self.display.get()
        # Clears the display
        self.display.delete(0, "end")
        # Prints the input
        print(self.num1)
        self.display.configure(state="readonly")


    def button_SUB_handler(self): # See button_ADD_handler()
        self.display.configure(state="normal")
        self.operation = "-"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print(self.num1)
        self.display.configure(state="readonly")

    def button_PERC_handler(self): # See button_ADD_handler()
        self.display.configure(state="normal")
        self.operation2 = "%"
        self.num3 = self.display.get()
        print("percentage")
        self.display.configure(state="readonly")
        self.button_EQUALS_handler()

    def button_SQUARE_handler(self): # See button_ADD_handler()
        self.display.configure(state="normal")
        self.operation = "square"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print("square")
        self.display.configure(state="readonly")
        self.button_EQUALS_handler()

    def button_ROOT_handler(self): # See button_ADD_handler()
        self.display.configure(state="normal")
        self.operation = "root"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print("root")
        self.display.configure(state="readonly")
        self.button_EQUALS_handler()

    def button_MUL_handler(self):
        self.display.configure(state="normal")
        self.operation = "*"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print(self.num1)
        self.display.configure(state="readonly")

    def button_DIV_handler(self):
        self.display.configure(state="normal")
        self.operation = "/"
        self.num1 = self.display.get()
        self.display.delete(0, "end")
        print(self.num1)
        self.display.configure(state="readonly")

    def button_EQUALS_handler(self):
        try:
            carry_on = 0
            self.display.configure(state="normal")
            # Convert num1 to a float so mathematical operations can be applied
            num1 = float(self.num1)
            print(self.num1)
            # Get info from display and store it in a variable
            num2 = self.display.get()
            num2 = float(num2)
            print(num2)
            # Create a variable to store result
        except ValueError:
            print("Needs a second Value")
            

        result = 0
        result = float(result)
        self.num3 = float(self.num3)
        self.num1 = float(self.num1)

        if self.operation2 == "%" and self.operation == "-":
            num3 = self.num3/100
            num4 = self.num1*num3
            result = self.num1-num4
            carry_on = 1
            
        elif self.operation2 == "%" and self.operation == "+":
            num3 = self.num3/100
            num4 = self.num1*num3
            result = self.num1+num4
            carry_on = 1

        elif self.operation2 == "%" and self.operation == "*":
            num3 = self.num3/100
            num4 = self.num1*num3
            result = self.num1*num4
            carry_on = 1

        elif self.operation2 == "%" and self.operation == "/":
            num3 = self.num3/100
            num4 = self.num1*num3
            result = self.num1/num4
            carry_on = 1
        
        elif self.operation == "root":
            num2 = math.sqrt(num1)
            result = num2

        elif self.operation == "square":
            result = num1*num1

            
        elif self.operation == "+": # Determine operation based on user input using if statments comparing self.operation
            if carry_on == 0:
                print("add")
                result = num1 + num2 # Do the maths
                print(result)
            else:
                print("carry on")

        elif self.operation == "-":
            if carry_on == 0:
                print("subtract")
                result = num1 - num2
                print(result)
            else:
                print("carry on...")

        elif self.operation == "*":
            if carry_on == 0:
                print("multiply")
                result = num1 * num2
                print(result)
            else:
                print("carry on...")

        elif self.operation == "/":
            if carry_on == 0:
              # You cannot divide by zero - ZeroDivisionError Exception Handling
                try:
                    print("divide")
                    result = num1 / num2
                    print(result)
                except ZeroDivisionError:
                    print("You cannot divide by zero!")
                    result = "Error!"
            else:
                print("carry on...")
                
        
        carry_on = 0
        self.display.delete(0, "end")       
        self.display.insert("end", result) # Show the result
        # Reset all variables
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0
        self.num1 = 0
        self.num2 = 0 
        self.operation = ""
        self.operation2 = ""
        self.display.configure(state="readonly")


root = Tk() # Setup the tkinter window


# Create an instance - allows the window class to use tkinter
app = Window(root)
app.pack()
# Extra code for GUI goes between root - Tk() and mainloop() -
def key(event):
    print("pressed", repr(event.char))
    press = event.char
    if press == "7":
        app.button_1.configure(state=ACTIVE)
        app.button_1_handler()
        app.after(50, lambda: app.button_1.config(state=NORMAL))

    elif press == "8":
        app.button_2.configure(state=ACTIVE)
        app.button_2_handler()
        app.after(50, lambda: app.button_2.config(state=NORMAL))

    elif press == "9":
        app.button_3.configure(state=ACTIVE)
        app.button_3_handler()
        app.after(50, lambda: app.button_3.config(state=NORMAL))
        
    elif press == "4":
        app.button_4.configure(state=ACTIVE)
        app.button_4_handler()
        app.after(50, lambda: app.button_4.config(state=NORMAL))
        
    elif press == "5":
        app.button_5.configure(state=ACTIVE)
        app.button_5_handler()
        app.after(50, lambda: app.button_5.config(state=NORMAL))
        
    elif press == "6":
        app.button_6.configure(state=ACTIVE)
        app.button_6_handler()
        app.after(50, lambda: app.button_6.config(state=NORMAL))
        
    elif press == "1":
        app.button_7.configure(state=ACTIVE)
        app.button_7_handler()
        app.after(50, lambda: app.button_7.config(state=NORMAL))
        
    elif press == "2":
        app.button_8.configure(state=ACTIVE)
        app.button_8_handler()
        app.after(50, lambda: app.button_8.config(state=NORMAL))
        
    elif press == "3":
        app.button_9.configure(state=ACTIVE)
        app.button_9_handler()
        app.after(50, lambda: app.button_9.config(state=NORMAL))
        
    elif press == "0":
        app.button_10.configure(state=ACTIVE)
        app.button_10_handler()
        app.after(50, lambda: app.button_10.config(state=NORMAL))
    elif press == ".":
        app.button_11.configure(state=ACTIVE)
        app.button_11_handler()
        app.after(50, lambda: app.button_11.config(state=NORMAL))
        
    elif press == "c":
        app.button_12.configure(state=ACTIVE)
        app.button_12_handler()
        app.after(50, lambda: app.button_12.config(state=NORMAL))
        
    elif press == "+":
        app.button_ADD.configure(state=ACTIVE)
        app.button_ADD_handler()
        app.after(50, lambda: app.button_ADD.config(state=NORMAL))
        
    elif press == "-":
        app.button_SUB.configure(state=ACTIVE)
        app.button_SUB_handler()
        app.after(50, lambda: app.button_SUB.config(state=NORMAL))
        
    elif press == "*":
        app.button_MUL.configure(state=ACTIVE)
        app.button_MUL_handler()
        app.after(50, lambda: app.button_MUL.config(state=NORMAL))
        
    elif press == "/":
        app.button_DIV.configure(state=ACTIVE)
        app.button_DIV_handler()
        app.after(50, lambda: app.button_DIV.config(state=NORMAL))
    elif press == "=":
        app.button_EQUALS.configure(state=ACTIVE)
        app.button_EQUALS_handler()
        app.after(50, lambda: app.button_EQUALS.config(state=NORMAL))
    elif press == "%":
        app.button_PERC.configure(state=ACTIVE)
        app.button_PERC_handler()
        app.after(50, lambda: app.button_PERC.config(state=NORMAL))
        
def returnButton(event):
     app.button_EQUALS.configure(state=ACTIVE)
     app.button_EQUALS_handler()
     app.after(50, lambda: app.button_EQUALS.config(state=NORMAL))
    

def clear(event):
    app.button_12.configure(state=ACTIVE)
    app.button_12_handler()
    app.after(50, lambda: app.button_12.config(state=NORMAL))
        

    
app.focus_set()
app.bind("<Key>", key)
app.bind("<Return>", returnButton)
app.bind("<BackSpace>", clear)

while app.operation == "+":
    print("hello there")

root.mainloop()

print("No don't leave!")
