import tkinter
import tkinter.ttk as ttk

pen = tkinter.Tk()

def merhaba():
    print('merhaba')

btn = ttk.Button(text='merhaba', command=merhaba)
btn.pack(padx=20, pady=20)

pen.mainloop()
