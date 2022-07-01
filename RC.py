    def cryptograpy_compression(self):
                
                self.name = "Author: Jurijus pacalovas"
                
                if namez=="c":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Deep = 1000
                        
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
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                 
                       

                  
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
                                
                                sda3=sda2
                                long_file=len(sda3)
                                sda10=""
                                sda9=""
                                sda5=""
                                fda5=""
                                sda4=""
                                sda6=""
                                sda7=""
                                sda12=""
                                sda19=""
                                sda10=sda3
                                predict=-1
                                
                                

                                cvf1=1
  
                                if cvf1==1:
                                    times_compression=0  
                                    compress_no=0
                                    compress_yes=0
                                    long2=len(sda3)
                                    Deep=long2//28
                                    times2=Deep
                                    
                                
                                    
                                    
                                    block_compression2=0
                                    
                                    start=-1
                                    while  times_compression!=times2:

                                                start=0
                                                blocks=16
                                                end=blocks
                                                
                                                find_matches1_number1=0
                                                find_matches1_number2=0
                                                find_matches1_number3=0   
                                                
                                                predict=predict+1
                                                if predict==16:
                                                    predict=0
                                                
                                                
                                                                                             
                                                                                                                                    
            
                                                block=0
                                                b=format(predict,'04b')
                                                
                                                Find=1
                                                block_compression1=0
                                                block_compression=0
                                                block_compression2=0
                                                long=len(sda3)
                                                #print(long)
                                                
                                                while block<long:
                                                                            str_find_tree_maches=sda3[block:block+blocks]
                                                    
                                                                            sub_info=b
                                                                            sub2=b
                                                                
                                                                            
                                                                            find_matches1=str_find_tree_maches.find(sub_info, start, end)
                                                                            find_matches1_1=int(find_matches1)

                                                                            if find_matches1_1==-1:
                                                                                Find=0 
                                                                            
                                                                            if find_matches1_1!=-1:
                                                                                
                                                                                find_matches1_number1=int(find_matches1)
                                       
                                                                                if find_matches1_1==0:

                                                                                    sda4=str_find_tree_maches[:0]+"00"+str_find_tree_maches[4:]

                                                                                elif find_matches1_1==2:

                                                                                    sda4=str_find_tree_maches[:2]+"01"+str_find_tree_maches[6:]

                                                                                elif find_matches1_1==4:
                                                                                    sda4=str_find_tree_maches[:4]+"10"+str_find_tree_maches[8:]

                                                                                elif find_matches1_1==6:
                                                                                    sda4=str_find_tree_maches[:6]+"11"+str_find_tree_maches[10:]

                                                                                Where=0
                                                                                 
                                                                                sub_info1="00"                                       
                                                                                find_matches2=str_find_tree_maches.find(sub_info1, start, end)
                                                                                find_matches1_2=int(find_matches2)
                                                                                if find_matches1_2==0:
                                                                                    Where=block+0

                                                                                sub_info1="01"                                       
                                                                                find_matches3=str_find_tree_maches.find(sub_info1, start, end)
                                                                                find_matches1_3=int(find_matches3)
                                                                                if find_matches1_3==2:
                                                                                    Where=block+2

                                                                                sub_info1="10"                                       
                                                                                find_matches3=str_find_tree_maches.find(sub_info1, start, end)
                                                                                find_matches1_3=int(find_matches3)
                                                                                if find_matches1_3==4:
                                                                                    Where=block+4

                                                                                sub_info1="11"                                       
                                                                                find_matches4=str_find_tree_maches.find(sub_info1, start, end)
                                                                                find_matches1_4=int(find_matches4)
                                                                                if find_matches1_4==6:
                                                                                    Where=block+6

                                                                                
                                                                                if Where!=0:
                                                                            
                                                                                    sda20=bin(Where)[2:]
                                                                                    lenf=len(sda20)
                                                                                    if lenf>21:
                                                                                        print("File too big")
                                                                                        
                                                                                        
                                                                                    
                                                                                    add_bits118=""
                                                                                    count_bits=21-lenf%21
                                                                                    z=0
                                                                                    if count_bits!=0:
                                                                                        if count_bits!=21:
                                                                                            while z<count_bits:
                                                                                                add_bits118="0"+add_bits118
                                                                                                z=z+1
                                                                                                                
                                                                                                                
                                                                                    sda19="1"+add_bits118+sda20+sda19
                                                                                
                                                                                                                     
                                                                            if Find!=0:
                                                                                
                                                                               
                                                                                sda6=sda6+sda4    
                                                                                compress_yes=compress_yes+1                                                                
                                                                          
                                                                                sda5=""
                                                                                sda7=""
                                                                                sda12=""
                                                                                sda4=""
                                                                                block_compression2=0
                                                                                Find=1
                                        
                                                                            elif Find==0:
                                                                                compress_no=compress_no+1
                                                                                #print(compress_no)
                                                                            
                                                                                block_compression=0
                                                                                block_compression1=0
                                                                                sda6=sda6+str_find_tree_maches
                                                                                
                                                                                sda5=""
                                                                                sda7=""
                                                                                sda12=""
                                                                                block_compression2=0
                                                                                Find=1
                                                                                    
                                                                            block=block+blocks
                                                                            #print(block)
                                                     
                                                times_compression=times_compression+1
                                                sda19="0"+sda19
                                                #print(times_compression)
                                                
                                                
                                                     
                                                    
            
                                                sda3=sda6
                                                
                                                #print(len(sda6))
                                                sda6=""
                                                
                                    long_after=len(sda3)
                                    print(long_after)
                                    print("Long after")
                                    print(long_file)
                                    print("Long before")
                                    if long_file<=long_after or long_after<=1:
                                        sda9="0"+sda10
                                    elif long_file>long_after:
                                        sda9="1"+sda3

                                    #print(sda9)
                                    long=len(sda19)    
                                    sda21=bin(long)[2:]
                                    lenf=len(sda21)
                                    if lenf>32:
                                            print("File too big")
                                                                                    
                                                                                   
                                                                                
                                    add_bits118=""
                                    count_bits=32-lenf%32
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=32:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                                
                                    sda22=add_bits118+sda21+sda19     
                                    sda9="1"+sda22+sda9

                                    
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

                                    sda24=bin(times2)[2:]
                                    lenf=len(sda24)
                                    if lenf>32:
                                            print("File too big")
                                                                                        
                                                                                        
                                                                                    
                                    add_bits118=""
                                    count_bits=32-lenf%32
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=32:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                                                                                                
                                                                                                                
                                    sda9=add_bits118+sda24+sda9
                                    
                                    
                                    
                                    


                                    
                                    print(compress_no)
                                    print("Not compress blocks")
                                    print(compress_yes)
                                    print("Compress blocks")
                                   
                                    n = int(sda9, 2)
                                
                                    qqwslenf=len(sda9)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                
                                    size_after=len(jl)
                                    print(size_after)
                                    print("size after")
                                
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
