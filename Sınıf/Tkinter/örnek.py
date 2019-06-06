import tkinter as tk

pencere = tk.Tk()

def çıkış():
    etiket['text'] = 'Elveda zalim dünya...'
    düğme['text'] = 'Bekleyin...'
    düğme['state'] = 'disabled'
    pencere.after(2000, pencere.destroy)


etiket = tk.Label(text='Merhaba Zalim Dünya')
etiket.pack()

düğme = tk.Button(text='Çık', command=pencere.destroy)
düğme.pack()

pencere.protocol('WM_DELETE_WINDOM', çıkış)

pencere.mainloop()
