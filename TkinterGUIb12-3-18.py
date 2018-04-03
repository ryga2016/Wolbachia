import os
os.chdir("c:\\Users\johnn\Dropbox\ProgrammingBioinfo\progIIProject")
import sys
from tkinter import *
from tkinter.filedialog  import askopenfilename
from tkinter.filedialog import asksaveasfile 
import BamReader

# save as a pyw to double click and run?


class wolbachiaGUI():

# Technically, everything occurs here. By simply running this file, 
# or calling this class, the gui will run.         
    def __init__(self):
        global master
        global e1 
        global e2 
        global e3
        global e4
        e3 = StringVar()
        e4 = StringVar()
        master = Tk()
# This turns the X button in the corner into a failsafe device.        
        master.protocol('WM_DELETE_WINDOW', wolbachiaGUI.on_exit)
        Label(master, text="inFile").grid(row=0)
        Label(master, text="outFile").grid(row=1)
#I'm unsure if the last part is needed; will investigate making the width variable to len(input)        
        e1 = Entry(master, width=100, textvariable=e3)
        e2 = Entry(master, width=100, textvariable=e4)
           
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
 # Creates buttons, doesn't run the methods imbedded within until clicked due to the lack of '()'   
        Button(master, text='...', command= wolbachiaGUI.fileI).grid(row=0,column=2, sticky=W, pady=4)
        Button(master, text='...', command= wolbachiaGUI.fileO).grid(row=1,column=2, sticky=W, pady=4)     
        Button(master, text='Run', command= wolbachiaGUI.RunReader).grid(row=3, column=2, sticky=W, pady=4)
        
        master.mainloop( )
        
#Dummy method    
    def RunReader():
        infile = str(e3)
        outfile = str(e4)
        BamReader.BamReader(infile, outfile)
        
# Button actions activate!
    def fileI():
        e3 = askopenfilename(initialdir='~')
        e1.insert(0, e3)
               
    def fileO():
        e4 = asksaveasfile(defaultextension=".txt")
        #e4.close()
        e2.insert(0, e4.name)
        

# Fail-safe method for actually closing the program. W/o, kernal err occurs. 
    @classmethod    
    def on_exit(self):
        master.destroy()
        master.quit()
        sys.exit
        
            
wolbachiaGUI()
   