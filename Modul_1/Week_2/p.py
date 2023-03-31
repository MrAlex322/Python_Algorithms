from tkinter import *

from tkinter import messagebox 

top = Tk()

top.geometry("200x100")

def binary_search(): 
    messagebox.showinfo("Hello", "Red Button clicked") 

def linear_search(): 
    messagebox.showinfo("Hello", "Red Button clicked") 


binary = Button(top,text = "Red",command = binary_search,activeforeground = "red",activebackground = "pink",pady=10)
linear = Button(top, text = "Blue",command = linear_search,activeforeground = "blue",activebackground = "pink",pady=10) 


binary.pack() 
linear.pack() 


top.mainloop()
