import os
import sys
try:
    import segno
except:
    os.system('pip install segno')
    import segno

text=sys.argv[1]
try: 
    ver=sys.argv[2]
    if(len(ver)==1):
        v=int(ver)
        edge=v*4+17
        offset=4
    elif(len(ver)==2):
        v=int(ver[1])
        edge=v*2+9
        offset=2
    else:
        print("version error")
        exit()
    
except IndexError:
    ver=3
    edge=ver*4+17
    offset=4


qr=segno.make(content=text, version=ver)
qr.save("out.png")
qr.save("out.txt")


file=open("out.txt", 'r')
f=file.readlines()
file.close()

out="{"
for i in f[offset:offset+edge]:
    out+='\t{'
    for j in i[offset:offset+edge]:
        if j=='\n':
            continue
        out+=j+', '
    out+='},\n'
out+="}"

f=open('out.txt', 'w')
f.write(out)
f.close()

f=open('out.txt', 'r')
for i in f:
    print(i)
f.close()
input()