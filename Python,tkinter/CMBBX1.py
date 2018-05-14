import tkinter as tk
import tkinter.ttk as ttk

def TAKE():
     global labelText,GreetingLabel
     if int(combo.get())>=18:
          GreetingLabel.destroy()
          labelText.set('Greeting: '+combo.get()+"$ Thank You! Have a good day!!")
          GreetingLabel=tk.Label(parent,text=labelText.get())
          GreetingLabel.place(x=40,y=200)
          print(str(combo.get()))
 
     else:
          GreetingLabel.destroy()
          labelText.set("Greeting: "+combo.get()+'$ Next,please')
          GreetingLabel=tk.Label(parent,text=labelText.get())
          GreetingLabel.place(x=40,y=200)
          print(combo.get())
 
parent=tk.Tk()
parent.title("Cofee Shop Patrons Greeting")
combo=ttk.Combobox(parent)
combo.place(x=50,y=100)
combo['values']=('1','4','18','40')
combo.current(2)
labelText=tk.StringVar()
labelText.set('Greeting:'+str(combo.get()))
GreetingLabel=tk.Label(parent,text=labelText)
GreetingLabel.place(x=40,y=200)
button=tk.Button(parent,command=TAKE,text='Calculate')
button.place(x=80,y=150)
GreetingLabel=tk.Label(parent,text=labelText.get())
GreetingLabel.place(x=40,y=200)
parent.geometry('300x300')
parent.mainloop()
