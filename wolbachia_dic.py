#        header=f1.readline() #skip the header
    for line in f1:
            fields=line.split()
            key=fields[0]
            GoodChromosomes.append(key)

for item in GoodChromosomes:
        print(item)

WbDict={}
ReadFile=open("/nobackup/rogers_research/OlgaData/wolOutputReads.sam", 'r')
for line in ReadFile:
        field=line.split()
        key1=field[2]
        key2=field[6]
        value=line
        if key1 in GoodChromosomes:
            if key1 in WbDict:
                print(key1)
                WbDict[key1].append(value)
            else:
                WbDict[key1]=[value]
        elif key2 in GoodChromosomes:
            if key2 in WbDict:
                print(key2)
                WbDict[key2].append(value)
            elif key2 not in WbDict:
                WbDict[key2]=[value]

#print(list(WbDict,d,file=outf))
for checkkey in list(WbDict):
    OutFile=open(checkkey+".reads", 'w')
    print(checkkey,file=OutFile)
#    print(WbDict[checkkey])
    for item in WbDict[checkkey]:
        print(item,file=OutFile, end="")
    # print(d,file=outf)
