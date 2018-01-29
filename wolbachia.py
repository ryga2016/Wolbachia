import sys
#Run the program as samtools view Foo.bam |python WbReads.py
#example line from bam file:
wolList=[]
for line in sys.stdin:
  # line="WUSI-EAS1562_0001:7:3:6539:13705#0	163	2L	1	0	48M	=	313	360	TGTGTTGGTAAAGCAGTTGTGTGTTGTTTAATACCGCTAT...''
  lineAsTokens=line.split()  #Now your code goes below.  We can work on it together if you want.
  # a=['WUSI-EAS1562_0001:7:3:6539:13705#0', '163', '2L', ... ]
  if a[6]=="NC_002978.6":
    wolList.append(line)
  if a[2]=="2L":
  	wolList.append(line)
print('# wolbachia lines found = ' + len(wolList))

#with 
outf=open('nobackup/rogers_research/OlgaData/wolOutputReads.sam', 'w')

for line in wolList:
    print(line, file=outf)
