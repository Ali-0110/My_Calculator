from tkinter import *

###### FUNCTIONS ######
def button_press(num):
    global equation_text
    equation_text= equation_text +str(num)
    label.config(text=equation_text)

def equals():
    global equation_text
    try:    
       total=str(eval(equation_text))
       label.config(text=total)
       equation_text=total    
    except ZeroDivisionError:
        label.config(text="ERROR")
        equation_text =""
    except SyntaxError:
        label.config(text="ERROR")
        equation_text =""    

def clear():
    global equation_text

    label.config(text=equation_text)


    equation_text = ""

###### Mainloop ######
window= Tk()
window.title("My Calculater")
window.geometry("570x600+100+200")
window.resizable(FALSE,FALSE)
window.configure(bg="#17161b")

equation_text =""


label=Label(window,text="",font=('consolas',20),
bg="white",width=45,height=2)
label.pack()

###### BUTTONS ######
Button(window, text="C",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(window, text="/",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("/")).place(x=150,y=100)
Button(window, text="%",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("%")).place(x=290,y=100)
Button(window, text="*",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("*")).place(x=430,y=100)

Button(window, text="7",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("7")).place(x=10,y=200)
Button(window, text="8",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("8")).place(x=150,y=200)
Button(window, text="9",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("9")).place(x=290,y=200)
Button(window, text="-",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("-")).place(x=430,y=200)

Button(window, text="4",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("4")).place(x=10,y=300)
Button(window, text="5",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("5")).place(x=150,y=300)
Button(window, text="6",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("6")).place(x=290,y=300)
Button(window, text="+",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("+")).place(x=430,y=300)

Button(window, text="1",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("1")).place(x=10,y=400)
Button(window, text="2",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("2")).place(x=150,y=400)
Button(window, text="3",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("3")).place(x=290,y=400)
Button(window, text="0",height=1,width=11,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press("0")).place(x=10,y=500)

Button(window, text=".",height=1,width=5,font=("arial",30,"bold"),fg="#fff",bg="#2a2d36",command=lambda: button_press(".")).place(x=290,y=500)
Button(window, text="=",height=3,width=5,font=("arial",30,"bold"),fg="#fff",bg="#fe9037",command=lambda: equals()).place(x=430,y=400)


window.mainloop()