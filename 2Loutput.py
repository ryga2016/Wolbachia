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

infile =
outfile =

fileObj = Keys2L(infile, outfile)
fileObj.Keysprint()
