from tkinter import *

formule = ""

def click(num):
    global formule
    formule = formule + str(num)
    equation.set(formule)

def equalclick():
    try:
        global formule
        result = str(eval(formule))
        equation.set(result)
        formule = result
    except:
        equation.set(" error ")
        formule = ""

def effacer():
    global formule
    formule = ""
    equation.set("")

if __name__ == "__main__":
    master = Tk()
    master.title("Calculatrice")
    master.geometry("375x315")
    equation = StringVar()
    formule_field = Entry(master, textvariable=equation)
    formule_field.grid(columnspan=4, pady=30, padx=20, ipadx=100, ipady=10)

    buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/", "."]
    row = 2
    col = 0
    for button in buttons:
        if button == "+":
            cmd = lambda: click("+")
        elif button == "-":
            cmd = lambda: click("-")
        elif button == "*":
            cmd = lambda: click("*")
        elif button == "/":
            cmd = lambda: click("/")
        elif button == ".":
            cmd = lambda: click(".")
        else:
            cmd = lambda button=button: click(button)
        btn = Button(master, text=button, command=cmd, height=2, width=10)
        btn.grid(row=row, column=col)
        col += 1
        if col > 2:
            col = 0
            row += 1
    minus = Button(master, text=' - ', command=lambda: click("-"), height=2, width=10)
    minus.grid(row=3, column=3)

    multiply = Button(master, text=' * ', command=lambda: click("*"), height=2, width=10)
    multiply.grid(row=4, column=3)

    equal = Button(master, text=' = ', command=equalclick, height=2, width=10)
    equal.grid(row=5, column=2)

    effacer = Button(master, text='effacer', command=effacer, height=2, width=10)
    effacer.grid(row=6, column='0')
    master.mainloop()
