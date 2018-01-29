from __future__ import print_function
with open('/Users/ryga2016/Desktop/Wolbachia/wolbachia_key') as f:
    ls=f.read().splitlines()
    ls





outf= open('/Users/ryga2016/Desktop/Wolbachia/dic_wolbachia_output', 'w')

d={}
GoodChromosomes=[]
with open('/Users/ryga2016/Desktop/Wolbachia/wolbachia_key') as f1:
#        header=f1.readline() #skip the header
        for line in f1:
            fields=line.split()
            key=fields[0]
			GoodChromosomes.append(key)
for item in GoodChromosomes:
        print(item)  #save to dic_wolbachia_output

#{k:d[k] for k in ls if k in d}
