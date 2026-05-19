import tkinter as tk
import time
import datetime
import threading

runing=True

class  myapp:
    def __init__(self,root:tk.Tk):
        global runing
        self.root=root
        self.root.title("progress")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.pro=tk.Entry(background="black",foreground="white",text="hello world")
        self.pro.pack(padx=10,pady=10)
        self.timers= threading.Thread(target=self.hello)
        self.timers.start()
    def hello(self):
        global runing
        while 1:
            self.pro.delete("0","end")
            a=str(datetime.datetime.now())
            aa=a.find(".")
            if aa>-1:
                a=a[:aa]
            self.pro.insert("0",a)
            
            time.sleep(1)
            if not(runing):
                break
        
        







root=tk.Tk()
apps=myapp(root)
root.mainloop()
runing=False