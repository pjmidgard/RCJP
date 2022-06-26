from time import time
cvf=0
import os
import binascii
self="'"


zzaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
aqw1=0
zsaqq=""
qqqwz=0
assx=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
add=0
m = []
p=0
namea=""
d=1
a=0
asd=""
b=0
szx=""
asf2="0b"
while b<1790:
    m+=[-1]
    b=b+1
k = []
wer=""
qtqweqw=""
numberschangenotexist = []
numbers = []
namez = input("for compress c or extract e? ")
#@Author Jurijus pacalovas
class compression:

    def cryptograpy_compression(self):
                
                self.name = "Author: Jurijus pacalovas"
                
                if namez=="c":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
           

                    nameas=name+".bin"
                
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    sw1=0
                    sw2=0
                    sw3=0
                    sw5=0
                    sw4=0
                    sw6=0
                    sw7=0
                    n1=0
                    n=0
                    n2=0
                    n3=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                      
                 
                       

                  
                        s=str(data)
                        
                     
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                                
                                e4=sda2[e2:e3]
                                
                                block=block+1
                                if assxw>=e3%2:
                                            if e4=="1":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""  
                                       
                                      
                                            if e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               
                                            elif e4=="1" and e3== e3%12:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="1" and e3== e3%13:
                                                sda3=sda3+"0"
                                                e4="1"
                                                e4=""
                                                
                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                    
                                                    
                                            if e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               

                                            elif e4=="1" and e3== e3%2:
                                                sda3=sda3+"0"
                                                e4="1"
                                                e4=""
                                                
                                            elif e4=="0" and e3== e3%2:
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                            elif e4=="1" and e3== e3%3:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                            elif e4=="0" and e3== e3%3:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                            elif e4=="1" and e3== e3%4:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""
                                            elif e4=="0" and e3== e3%4:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""                                                             
                                            elif e4=="0" and e3== e3%5:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="1" and e3== e3%5:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                    
                                            elif e4=="0" and e3== e3%6:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="1" and e3== e3%6:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""                                                                                    
                                            elif e4=="0" and e3== e3%7:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="0" and e3== e3%7:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""    
                                            elif e4=="0" and e3== e3%8:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="0" and e3== e3%8:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""    
                                            elif e4=="0" and e3== e3%9:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""   
                                                                           
              
                                            elif e4=="1" and e3== e3%9:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""                                                                                                                                                                                                                                                                                                                                                        
                                            elif e4=="0" and e3== e3%11:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="0" and e3== e3%11:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""      
                                            elif e4=="1" and e3 ==e3%13:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                    
                                            elif e4=="1" and e3 ==e3%14:
                                                    sda3=sda3+"0"
                                                    e4="1"
                                                    e4=""
                                                    
                                                    
                                                    
                                            elif e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                            if assxw>1:
                                                if e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""

                                                if e4=="1":
            	                                    
            		                           
                                             

                                
                                                   if e4=="1" and e3== e3%7:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%16:
                                                        sda3=sda3+"0"
                                                        e4="1"
                                                        e4=""
                                                    
                                                   elif e4=="1" and e3== e3%15:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%14:
                                                        sda3=sda3+"0"
                                                        e4="1"
                                                        e4=""
                                                        
                                               
                                                   elif e4=="1" and e3== e3%13:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""

                                
                                if e4=="1" and e3== e3%9+assxw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                
                                elif e4=="1" and e3== e3%8+assxw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%7+sw2:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%8+assxw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%7+sw2:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw2:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""   
                                
                                elif e4=="1" and e3== e3%7+sw1:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw1:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%7+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                
                                elif e4=="1" and e3== e3%5+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                elif e4=="1" and e3== e3%2+sw7:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4="" 
                                elif e4=="1" and e3== e3%2+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4="" 
                                
                                elif e4=="1" and e3== e3%18+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""	
                                elif e4=="1" and e3== e3%18+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%17+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
   
                                elif e4=="1" and e3== e3%4+sw4:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw4:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""                                  
                                elif e4=="1" and e3== e3%4+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                elif e4=="1" and e3== e3%23+n or e4=="1" and e3== e3%23+n1 or e4=="1" and e3== e3%23+n2:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""	
                                 
                                elif e4=="1" and e3== e3%22+n1:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                                                        
                                elif e4=="1" and e3== e3%2+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
                                        
                                elif e4=="1":
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0":
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
	                                                  
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=cvf+1

                                    cvf=sw
                                    cvf=sw1
                                    cvf=sw2
                                    cvf=sw3
                                    sw=sw+n+3
                                    sw1=sw1+n+4
                                    sw2=sw2+n+1
                                    sw3=sw3+n+3
                                    
                                    sw4=sw4+n
                                    
                                    n=n+7
                                    
                                    sw5=sw4+n
                                    
                                    n1=n1+5
                                    
                                    sw5=sw4+n1
                                    
                                    sw4=sw4+n1
                                    
                                    sw=sw+n+3
                                    sw1=sw1+n1+4
                                    sw2=sw2+n1+1
                                    sw3=sw3+n1+3
                                    
                                    sw5=sw4+n
                                    
                                    n1=n1+5
                                    
                                    sw6=sw4+n2
                                    
                                    sw6=sw6+n2
                                    
                                    sw=sw+n+3
                                    sw1=sw1+n2+1
                                    sw2=sw2+n2+3
                                    sw3=sw3+n2+2
                                    
                                    n2=n2+8
                                    
                                    n3=n3+2
                                    sw7=n3
                                    
                                    
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+1
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                    times_compression=0  
                                    compress_no=0
                                    compress_yes=0
                                    long2=len(sda3)
                                    times2=long2
                                    sda9=""
                                    block_compression2=0
                                    
                                    start=-1
                                    while  times_compression!=times2:

                                                start=0
                                                end=128
                                                sda5=""
                                                sda4=""
                                                sda6=""
                                                sda7=""
                                                
            
                                                block=0
                                                Find=0
                                                block_compression1=0
                                                block_compression=0
                                                block_compression2=0
                                                long=len(sda3)
                                                
                                                while block<long:
                                                                            str_find_tree_maches=sda3[block:block+128]
                                                    
                                                                            sub_info="0000"
                                                                            sub2="0000" 
                                                                
                                                                            
                                                                            find_matches1=str_find_tree_maches.find(sub_info, start, end)
                                                                            
                                                                                            
                                                    
                                                                            if find_matches1!="-1":
                                                                                
                                                                                find_matches1_number1=int(find_matches1)
                                                                                if block_compression2==0:
                                                                                    block_compression2=1
                                                                                
                                                                                
                                                                            find_matches1=str_find_tree_maches.find(sub2, start+4, end)
                                                                            
            
                                                                            if find_matches1!="-1":
                                                                                    
                                                                                    find_matches1_number2=int(find_matches1)
                                                                                    if block_compression2==1:
                                                                                        block_compression2=2
                                                    
                                                                            find_matches1=str_find_tree_maches.find(sub2, find_matches1_number1+4, end)
                                                                            
                                                                            find_matches1_number3=int(find_matches1)
                                                                            if find_matches1!="-1":
                                                                                Find=1
                                                                                if block_compression2==2:
                                                                                    block_compression2=3
                                            
                                                                            sub_info3=str_find_tree_maches[find_matches1_number3+4:find_matches1_number3+7]
                                                                            
                                                                            find_matches_1=str_find_tree_maches.find("000000", find_matches1_number1+4, end)
                                                                            if find_matches_1=="-1":  
                                                                                             Find=0  
                                                                            find_matches_2=str_find_tree_maches.find("001001", find_matches1_number1+4, end)
                                                                            if find_matches_2=="-1":  
                                                                                             Find=0    
                                                                            find_matches_3=str_find_tree_maches.find("010010", find_matches1_number1+4, end)
                                                                            if find_matches_3=="-1":  
                                                                                             Find=0   

                                                                            find_matches_4=str_find_tree_maches.find("011011", find_matches1_number1+4, end)
                                                                            if find_matches_4=="-1":  
                                                                                             Find=0
                                                                            find_matches_5=str_find_tree_maches.find("100100", find_matches1_number1+4, end)
                                                                            if find_matches_5=="-1":  
                                                                                             Find=0
                                                                            find_matches_6=str_find_tree_maches.find("101101", find_matches1_number1+4, end)
                                                                            if find_matches_6=="-1":  
                                                                                             Find=0
                                                                            find_matches_7=str_find_tree_maches.find("110110", find_matches1_number1+4, end)
                                                                            if find_matches_7=="-1":  
                                                                                             Find=0  
                                                                            find_matches_8=str_find_tree_maches.find("111111", find_matches1_number1+4, end)
                                                                            if find_matches_8=="-1":  
                                                                                             Find=0        
                                                                                                                       
                                                                            if Find==1:
                                                                                Find=0
                                                                                
                                                                                sda4=str_find_tree_maches[:find_matches1_number3-4]+sub_info3+str_find_tree_maches[find_matches1_number3:]
                                                                                sda5=sda5+sda4
                                                                                if block_compression==0:
                                                                                    block_compression=1
                                                                                elif block_compression==1:
                                                                                    block_compression=2
                                                                        
                                                                                sda7=str_find_tree_maches        
                                                                                block_compression1=block_compression1+1 
                                                                                if block_compression==block_compression1 and block_compression1==2 and block_compression2==3:
                                                                                    compress_yes=compress_yes+1
                                                                                    block_compression=0
                                                                                    block_compression1=0
                                                                                    sda6=sda6+"0"+sda5
                                                                                    sda5=""
                                                                                    sda7=""
                                                                                    block_compression2=0
                                        
                                                                                if block_compression!=block_compression1 and block_compression1==2 and block_compression2!=3:
                                                                                    compress_no=compress_no+1
                                                                                    block_compression=0
                                                                                    block_compression1=0
                                                                                    sda6=sda6+"1"+sda7
                                                                                    sda5=""
                                                                                    sda7=""
                                                                                    block_compression2=0
                                                                                    
                                                                                block=block+128
                                                     
                                                times_compression=times_compression+1      
                                                if block_compression==block_compression1 and block_compression1==1 and block_compression2==3:
                                                    compress_no=compress_no+1
                                                    block_compression=0
                                                    block_compression1=0
                                                    sda6=sda6+"1"+sda7
                                                    sda5=""
                                                    sda7=""
                                                    block_compression2=0
                                        
                                                if block_compression!=block_compression1 and block_compression1==1 and block_compression2!=3:
                                                    compress_no=compress_no+1
                                                    block_compression=0
                                                    block_compression1=0
                                                    sda6=sda6+"1"+sda7
                                                    sda5=""
                                                    sda7=""
                                                    block_compression2=0
                                                sda3=sda6
                                                sda9=sda6
                                                sda6=""
                                                 
                                    sda9="1"+sda9

                                    
                                    lenf=len(sda9)
                                    
                                    add_bits118=""
                                    count_bits=8-lenf%8
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=8:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                                                
                                                                
                                    sda9=add_bits118+sda9

                                    sda8=bin(times2)[2:]
                                    lenf=len(sda8)
                                    if lenf>40:
                                        print("size file is too big")
                                        x3=0.0
                                        return print(x3)
                                        
                                    
                                    add_bits118=""
                                    count_bits=40-lenf%40
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=40:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                                                
                                                                
                                    sda9=add_bits118+sda8+sda9
                                    
                                    print(compress_no)
                                    print(compress_yes)
                                   
                                    n = int(sda9, 2)
                                
                                    qqwslenf=len(sda9)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

    def cryptograpy_unpack(self):                      
                 if namez=="e":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    Portal=2
                    namea="file.W"
                    namem=""
                    namema="?"
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    nac=len(nameas)
                    
            
                    
                    
                    nac=len(nameas)
                    sw1=0
                    sw2=0
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    sw3=0
                    sw4=0
                    sw5=0
                    sw6=0
                    sw7=0
                    n=0
                    n1=0
                    n2=0
                    n3=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data = binary_file.read()
                     
                                             
                                             
                        
                        
                        
                        		

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                                
                                e4=sda2[e2:e3]
                                
                                block=block+1 
                                
                                if assxw>=e3%2:
                                            if e4=="1":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""  
                                       
                                      
                                            if e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               
                                            elif e4=="1" and e3== e3%12:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="1" and e3== e3%13:
                                                sda3=sda3+"0"
                                                e4="1"
                                                e4=""
                                                
                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                    
                                                    
                                            if e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               

                                            elif e4=="1" and e3== e3%2:
                                                sda3=sda3+"0"
                                                e4="1"
                                                e4=""
                                                
                                            elif e4=="0" and e3== e3%2:
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                            elif e4=="1" and e3== e3%3:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                            elif e4=="0" and e3== e3%3:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                            elif e4=="1" and e3== e3%4:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""
                                            elif e4=="0" and e3== e3%4:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""                                                             
                                            elif e4=="0" and e3== e3%5:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="1" and e3== e3%5:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                    
                                            elif e4=="0" and e3== e3%6:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="1" and e3== e3%6:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""                                                                                    
                                            elif e4=="0" and e3== e3%7:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="0" and e3== e3%7:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""    
                                            elif e4=="0" and e3== e3%8:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="0" and e3== e3%8:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""    
                                            elif e4=="0" and e3== e3%9:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""   
                                                                           
              
                                            elif e4=="1" and e3== e3%9:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""                                                                                                                                                                                                                                                                                                                                                        
                                            elif e4=="0" and e3== e3%11:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""   
                                                                           
                                            elif e4=="0" and e3== e3%11:
                                                    sda3=sda3+"1"
                                                    e4="0"
                                                    e4=""      
                                            elif e4=="1" and e3 ==e3%13:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                    
                                            elif e4=="1" and e3 ==e3%14:
                                                    sda3=sda3+"0"
                                                    e4="1"
                                                    e4=""
                                                    
                                                    
                                                    
                                            elif e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                            if assxw>1:
                                                if e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""

                                                if e4=="1":
            	                                    
            		                           
                                             

                                
                                                   if e4=="1" and e3== e3%7:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%16:
                                                        sda3=sda3+"0"
                                                        e4="1"
                                                        e4=""
                                                    
                                                   elif e4=="1" and e3== e3%15:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%14:
                                                        sda3=sda3+"0"
                                                        e4="1"
                                                        e4=""
                                                        
                                               
                                                   elif e4=="1" and e3== e3%13:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""

                                
                                if e4=="1" and e3== e3%9+assxw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                
                                elif e4=="1" and e3== e3%8+assxw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%7+sw2:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%8+assxw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%7+sw2:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw2:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""   
                                
                                elif e4=="1" and e3== e3%7+sw1:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw1:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%7+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                
                                elif e4=="1" and e3== e3%5+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                elif e4=="1" and e3== e3%2+sw7:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4="" 
                                elif e4=="1" and e3== e3%2+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4="" 
                                
                                elif e4=="1" and e3== e3%18+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""	
                                elif e4=="1" and e3== e3%18+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%17+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
   
                                elif e4=="1" and e3== e3%4+sw4:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw4:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""                                  
                                elif e4=="1" and e3== e3%4+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                elif e4=="1" and e3== e3%23+n or e4=="1" and e3== e3%23+n1 or e4=="1" and e3== e3%23+n2:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""	
                                 
                                elif e4=="1" and e3== e3%22+n1:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                                                        
                                elif e4=="1" and e3== e3%2+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
                                        
                                elif e4=="1":
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0":
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""
	                                                  
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=sw
                                    cvf=sw1
                                    cvf=sw2
                                    cvf=sw3
                                    sw=sw+n+3
                                    sw1=sw1+n+4
                                    sw2=sw2+n+1
                                    sw3=sw3+n+3
                                    
                                    sw4=sw4+n
                                    
                                    n=n+7
                                    
                                    sw5=sw4+n
                                    
                                    n1=n1+5
                                    
                                    sw5=sw4+n1
                                    
                                    sw4=sw4+n1
                                    
                                    sw=sw+n+3
                                    sw1=sw1+n1+4
                                    sw2=sw2+n1+1
                                    sw3=sw3+n1+3
                                    
                                    sw5=sw4+n
                                    
                                    n1=n1+5
                                    
                                    sw6=sw4+n2
                                    
                                    sw6=sw6+n2
                                    
                                    sw=sw+n+3
                                    sw1=sw1+n2+1
                                    sw2=sw2+n2+3
                                    sw3=sw3+n2+2
                                    
                                    n2=n2+8
                                    
                                    n3=n3+2
                                    sw7=n3
                                    
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+1
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                   
                                    n = int(sda3, 2)
                                
                                    qqwslenf=len(sda3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                 
                               
                                    sssssw=len(jl) 
                                  
                                   

                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                    
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

                                


 
                  
self=""                                
d=compression()
    
xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)
