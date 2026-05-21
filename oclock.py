import tkinter as tk
import time
import datetime
import threading
global runing 
runing=True

class  myapp:

    def __init__(self,root:tk.Tk,title:str,blackgrounds:str="black",foregrounds:str="white",w:int=650,h:int=480):
        global runing
        self.root=root
        self.root.title(title)
        self.root.geometry(str(w)+"x"+str(h))
        self.root.configure(background=blackgrounds)
        self.pro=tk.Entry(background=blackgrounds,foreground=foregrounds,text="                 ")
        self.pro.pack(padx=10,pady=10)
        self.timers= threading.Thread(target=self.hello)
        self.timers.start()
    def hello(self):
        global runing
        while 1:
            try:
                a=str(datetime.datetime.now())
                aa=a.find(".")
                if aa>-1:
                    a=a[:aa]
                if not(runing):
                    break
                self.pro.delete("0","end")
                self.pro.insert("0",a)
                if not(runing):
                    break
                time.sleep(1)
                if not(runing):
                    break
            except:
                break
        






def ocloks(title:str="clock",blackground:str="black",foreground:str="white",w:int=650,h:int=480):
    root=tk.Tk()
    apps=myapp(root,title,blackground,foreground,w,h)
    root.mainloop()
    runing=False
    time.sleep(3)