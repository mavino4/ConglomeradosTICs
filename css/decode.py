import os
import re

os.system("ls css/*.css > list.txt")

lista = open("list.txt","r")
for arch in lista: 
    css = open("%s" % (arch[:-1]),"r") 
    a = css.readline()
    #a = a[:-1]
    i =0
    b = ""
    while (i < len(a)):
        #print(a[i], i)
        if a[i] =="%":   
            b+= (chr(int(a[i+1:i+3],16)))
            i+=2
        else:
            i+=1
            try:
                if a[i] != "%":
                    b+=a[i]
            except IndexError:
                pass


    #print(b)
    file=  open("%sd.css" %(arch[:-5]),"w") 
    file.write(b[:-1]) 
    file.close()

## extrayendo las tipografias () 

"""
md = open("salida3.css", "r" )
# Abriendo variables para JS
os.system("python -c \"#Puerba de salida\" > indextype.html")
output = open("indextype.html","w+")
counterttf = 1 
for line in md:
    line1 = line
    x =re.findall("^src: url\(data:application*",line1)
    y =re.findall("rel=\"stylesheet\" />",line1)
    if x != []:
        print(x)
        line2 = line1[50:-21]
        #line2 = line1[51:-12]
        os.system("python -c \"#Abriendo datos\" > Type%s.ttf" % (counterttf))
        file = open("Type%s.ttf" % (counterttf), "w+")
        file.writelines(line2)
        file.close()
        counterttf+=1
    else:
        output.writelines(line) 
"""