"""
このファイルに解答コードを書いてください
"""
a = input()
a = int(a)
b=[]
c=[]
f = open("input.txt",'r')

for line in f:
#    print(line)
    items = line[:-1].split(':')
    b.append(int(items[0]))
    c.append((items[1]))

dct = dict(zip(b,c))
dct = sorted(dct.items())
b = sorted(b)
for i in b:
    if i%a==0:
        d,e=dct[i%a]
        print(i,":",e)
    else:
        print(a)