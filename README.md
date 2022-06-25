# RCJP
RLE random with zero compression 
RCJP

Algorithm RCJP:
1. Spring-109 Reverso:
start from %2 like this:
[C]
if assxw>=e3%2:  
[/C]
       
Continue             
                              

                                               

                                            
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

[/C]
RLE find three matches 3 that "0000" matches change to two next three block 128 bits
