import tkinter as tk

class Pencere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol('WM_DELETE_WINDOW', self.çıkış)

        self.etiket = tk.Label(text='Merhaba Zalim Dünya')
        self.etiket.pack()

        self.düğme = tk.Button(text='Çık', command=self.çıkış)
        self.düğme.pack()

    def çıkış(self):
        self.etiket['text'] = 'Elveda zalim dünya...'
        self.düğme['text'] = 'Bekleyin...'
        self.düğme['state'] = 'disabled'
        self.after(2000, self.destroy)

pencere = Pencere()
pencere.mainloop()
