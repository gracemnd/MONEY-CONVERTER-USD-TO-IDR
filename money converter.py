import tkinter as tk

def usd_to_idr():
    jumlah=textbox.get()
    dollar=float(jumlah)*14405.5
    text.set("Rp." + str(dollar))
    idr.config(font=('Calibri',40,"bold"),fg="red")


window=tk.Tk()
window.title("USD TO IDR CONVERTER")
window.geometry("500x300")

#membuat label USD
usd=tk.Label(window,text="USD",font=('Calibri',40,"bold"))
usd.pack()

#membuat text box
textbox=tk.Entry(window,font=('Calibri',20,"bold"),width=30,justify=tk.CENTER)
textbox.pack()

#membuat tombol klik
klik=tk.Button(window,text="TO",command=usd_to_idr)
klik.pack()

text=tk.StringVar()
text.set("IDR")

#membuat label IDR
idr=tk.Label(window,text="IDR",font=('Calibri',40,"bold"),textvariable=text)
idr.pack()

window.mainloop()