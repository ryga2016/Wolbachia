from tkinter import *
from tkinter.filedialog  import askopenfilename 

class wolbachiaGUI():
    
    def __init__():
        master = Tk()
        Label(master, text="inFile").grid(row=0)
        Label(master, text="outFile").grid(row=1)
        
        e1 = Entry(master)
        e2 = Entry(master)
        
        e1.grid(row=0, column=1)
        #e3.grid(row=0, column=2)
        e2.grid(row=1, column=1)
        #e4.grid(row=1, column=2)
        
        Button(master, text='...', command=fileIO).grid(row=0,column=2, sticky=W, pady=4)
        
        Button(master, text='...', command=fileIO).grid(row=1,column=2, sticky=W, pady=4)
        
        Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
        
        Button(master, text='Run', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
        
        mainloop( )
        print(e1.get(), e2.get())

    def show_entry_fields():
    # wolbachiaRead(e1)
    # wolbachiaOut(e2) 
    
    
    def fileIO():
            choosen = askopenfilename(initialdir='~')
            e1 = self.text.insert(END, open(self.choosen).read())
            

    
   