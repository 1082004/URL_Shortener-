import pyperclip
import pyshorteners
from tkinter import *

App = Tk()
App.geometry("400x360")
App.title("URL Shortener | AYMEN DEV")
#myApp.resizable(False,False)
url = StringVar()
url_address = StringVar()

def urlshort():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get
    pyperclip.copy(url_short)

Label(App,text="URL Shortener",font="Courier 30 bold").pack(pady=15)
Entry(App,textvariable=url).pack(pady=5)
Button(App,text="Generate Short URL", command=urlshort,fg="green").pack(pady=20)
Label(App,text="URL After Short",font="Courier 30 bold").pack(pady=15)
Entry(App,textvariable=url_address).pack(pady=10)
Button(App,text="Copy URL", command=copyurl,fg="green").pack(pady=10)
App.mainloop()
        
        
