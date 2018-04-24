import os
# Defines where the dir starts from (Home Dir)
os.chdir("c:\\Users\johnn\Dropbox\ProgrammingBioinfo\progIIProject")
import sys
from tkinter import *
from tkinter.filedialog  import askopenfilename
from tkinter.filedialog import asksaveasfile 


class wolbachiaGUI():
    
    

# Technically, everything occurs here. By simply instantiating this class obj, 
# or calling this class, the gui will run.         
    def __init__(self):
        global master
        global e1 
        global e2 
        global e3
        global e4
        # e3 = None
        # e4 = None
        # global infile
        # global outfile
        self.infile = None
        self.outfile = None
        self.e3 = StringVar()
        self.e4 = StringVar()
        master = Tk()
# This turns the X button in the corner into a failsafe device.        
        master.protocol('WM_DELETE_WINDOW', wolbachiaGUI.on_exit)
        Label(master, text="inFile").grid(row=0)
        Label(master, text="outFile").grid(row=1)
        e1 = Entry(master, width=100, textvariable=str(e3))
        e2 = Entry(master, width=100, textvariable=str(e4))
           
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
 # Creates buttons, doesn't run the methods imbedded within until clicked due to the lack of '()'   
        Button(master, text='...', command= self.fileI).grid(row=0,column=2, sticky=W, pady=4)
        Button(master, text='...', command= self.fileO).grid(row=1,column=2, sticky=W, pady=4)     
        Button(master, text='Run', command= self.RunReader).grid(row=3, column=2, sticky=W, pady=4)
        
        master.mainloop( )
        
#Run method for backend computation of 'matches' 
    def RunReader(self):
        # infile = str(e3)
        # outfile = str(e4)
        self.BamReaderRun()
        print(str(self.infile))
        print(str(self.outfile))
        self.BamPrint()
        
        
# Button actions activate!
    def fileI(self):
        e3 = open(askopenfilename(initialdir='~'), 'r')
        self.infile = e3
        e1.insert(0, e3.name)
               
    def fileO(self):
        e4 = asksaveasfile(defaultextension=".txt")
        self.outfile = e4
        e2.insert(0, e4.name)
        

# Fail-safe method for actually closing the program. W/o, kernal err occurs. 
    @classmethod    
    def on_exit(self):
        master.destroy()
        master.quit()
        sys.exit
        
### End of GUI software
                                
#         
# class BamReader():
#     outfile = None
#     infile = None
# 
#     def __init__(self, inF, outF):
#         self.infile = inF
#         self.outfile = outF
#         self.BamReaderRun()
#         print('poo')

    def BamReaderRun(self):
        with open(self.infile.name, 'r') as f1:
            with open(self.outfile.name, 'w+') as f2:

                print('starting...')
                wolList = []
                # outf = open('/nobackup/rogers_research/OlgaData/wolOutputReads.bam', 'w')
                # outf = open(self.outfile.name, 'w')
                # for line in sys.stdin:
                for line in f1:
        
                    lineOfBamFiles = line.split()
                    if lineOfBamFiles[3] == "NC_002978.6":
                            # print(line, file = outf , end="")
                            print(line, file = f2, end="")
                    elif lineOfBamFiles[6] == "NC_002978.6":
                            print(line, file = f2, end="")
                            # print (line, file = outf, end="")


    def BamPrint(self):
        print(self.outfile.name) 
        
###        
        
class Keys():
    outfile = None

    # infile = None

    def __init__(self, inF, outF):
        infile = inF
        outfile = outF
        self.Keys(infile, outfile)

    @classmethod
    def Keys2L(self, infile, outfile):
        with open(infile, 'r') as f1:
            with open(outfile, 'w+') as f2:


                with open('/nobackup/rogers_research/OlgaData/2lKeys') as f:
                    ls = f.read().splitlines()
                    header = f.read()
                    ls
                
            
            
            outf = open('/nobackup/rogers_research/OlgaData/2L_output', 'w')
            
            
            ReadDict = {}
            ReadFile = open("/nobackup/rogers_research/OlgaData/2L.reads", 'r')
            
            foo = ReadFile.readline()
            
            binsize = 100


    def reads(self, ):
        for read in ReadFile:
            fields = read.split()
    #        print(fields)
            position = int(fields[7])
            key1 = position - (position % binsize)
            value = read
            if key1 in ReadDict:
                    ReadDict[key1].append(value)
            else:
                ReadDict[key1] = [value]
    
    
    def checkkey(self, ):
        for checkkey in list(ReadDict):
            OutFile = open(str(checkkey) + ".reads", 'w')
            print(checkkey, file=OutFile)
        #    print(ReadDict[checkkey])
        for item in ReadDict[checkkey]:
            print(item, file=OutFile, end="")
        # print(d,file=outf)
    
        @classmethod
        def Keys(self):
            print(self.outfile)    

# RunTime           
wolbachiaGUI()
   