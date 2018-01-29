for read in ReadFile:
        fields=read.split()
#        print(fields)
        position=int(fields[7])
        key1=position - (position % binsize)
        value=read
        if key1 in ReadDict:
                ReadDict[key1].append(value)
        else:
            ReadDict[key1]=[value]    #create Dictionary entry

#print(list(ReadDict,d,file=outf))
for checkkey in list(ReadDict):
    OutFile=open(str(checkkey)+".reads", 'w')
    print(checkkey,file=OutFile)
#    print(ReadDict[checkkey])
    for item in ReadDict[checkkey]:
        print(item,file=OutFile, end="")
    # print(d,file=outf)             
