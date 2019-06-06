import tkinter
import tkinter.ttk as ttk

pen = tkinter.Tk()

btn = ttk.Button(text='merhaba', command=lambda: print('merhaba'))
btn.pack(padx=20, pady=20)

pen.mainloop()
