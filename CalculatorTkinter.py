from tkinter import *
#For Tkinter

window = Tk()
#This is where the program will create a window for the calculator
window.geometry = ("420x420")
window.title("Basic Calculator")
icon = PhotoImage(file="clogo.png")
window.iconphoto(True, icon)
window.config(bg="white")


def buttonClick(number): #This function will take the number and add it to the operator variable and set the input_value to the operator variable
    global operator
    operator = operator + str(number)
    input_value.set(operator)
    

def buttonClear(): #This function will clear the operator variable and set the input_value to the operator variable
    global operator
    operator = ""
    input_value.set("")
    

def buttonEqual(): #This function will evaluate the operator variable and set the input_value to the result and clear the operator variable
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""

    
#variables for the calculator
operator = ""
input_value = StringVar()

#This is for the screen of the calculator
display_text = Entry(window, font=("arial", 15, "bold"), textvariable=input_value, bd=15, insertwidth=4, width=20, borderwidth=20, justify=RIGHT)
display_text.grid(columnspan=4)

#This is for rows 1,7,8,9 and +

btn_7 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="7", command=lambda: buttonClick(7))
btn_7.grid(row=1,column=0)

btn_8 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="8", command=lambda: buttonClick(8))
btn_8.grid(row=1,column=1)

btn_9 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="9", command=lambda: buttonClick(9))
btn_9.grid(row=1,column=2)

btn_add = Button(window,padx=7.2,bd=8,fg="black",font=("arial", 20, "bold"), text="+" , command=lambda: buttonClick("+"))
btn_add.grid(row=1,column=3)

#This is for rows 4,5,6, and -

btn_4 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="4", command=lambda: buttonClick(4))
btn_4.grid(row=2,column=0)

btn_5 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="5", command=lambda: buttonClick(5))
btn_5.grid(row=2,column=1)

btn_6 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="6", command=lambda: buttonClick(6))
btn_6.grid(row=2,column=2)

btn_minus = Button(window,padx=7.2,bd=8,fg="black",font=("arial", 20, "bold"), text="-", command=lambda: buttonClick("-"))
btn_minus.grid(row=2,column=3)

#This is for rows 1,2,3, and *

btn_1 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="1" , command=lambda: buttonClick(1))
btn_1.grid(row=3,column=0)

btn_2 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="2" , command=lambda: buttonClick(2))
btn_2.grid(row=3,column=1)

btn_3 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="3", command=lambda: buttonClick(3))
btn_3.grid(row=3,column=2)

btn_times = Button(window,padx=7.2,bd=8,fg="black",font=("arial", 20, "bold"), text="*", command=lambda: buttonClick("*"))
btn_times.grid(row=3,column=3)

# This is for 0 C = /

btn_0 = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="0" , command=lambda: buttonClick(0))
btn_0.grid(row=4,column=0)

btn_c = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="C", command=buttonClear)
btn_c.grid(row=4,column=1)

btn_equals = Button(window,padx=7,bd=8,fg="black",font=("arial", 20, "bold"), text="=", command=buttonEqual)
btn_equals.grid(row=4,column=2)

btn_divide = Button(window,padx=7.2,bd=8,fg="black",font=("arial", 20, "bold"), text="/", command=lambda: buttonClick("/"))
btn_divide.grid(row=4,column=3)

window.mainloop() #main loop

