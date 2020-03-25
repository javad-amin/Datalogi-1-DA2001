import tkinter as tk
import calcCommand

def printfunc(a):
    entry.delete(0, tk.END)
    entry.insert(tk.END, a)

calcCommand.atCalcPrint(printfunc)

root = tk.Tk()
root.title("Enkel kalkylator")

inputs = [ str(i) for i in range(0, 10) ] + [ '.' ]
def click(key):
    try:
        if key == 'push':
            calcCommand.validate([ entry.get() ])
            entry.delete(0,tk.END)
        elif key == 'sluta':
            root.destroy()
        elif key == 'töm':
            entry.delete(0,tk.END)
            calcCommand.clearStack()
        else:
            if key in inputs:
                entry.insert(tk.END, key)
            else:
                calcCommand.validate([ key ])
                calcCommand.doCommands()
    except  calcCommand.CalcError as e:
        printfunc(e)

btn_list = [
'7',  '8', '9', '-', '+',
'4',  '5', '6', '/', '^', 
'1',  '2', '3', '*', 'push', 
'0',  '.',  '=', 'töm', 'sluta' ]

# Skapa alla knappar i en enda loop
i = 5

for b in btn_list:
    r, c = divmod(i, 5)
    rel = 'ridge'
    cmd = lambda x=b: click(x)
    tk.Button(root,text=b,width=10,height=5,relief=rel,command=cmd)\
      .grid(row=r,column=c)
    i += 1

# använd en Entry widget som editerbar display
entry = tk.Entry(root, width=33, bg="grey", font="Helvetica 20")
entry.grid(row=0, column=0, columnspan=5)

root.mainloop()
