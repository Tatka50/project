
import pdb

print('Введите натуральное число')
chi1=input()
chi=int(chi1)
print('Введите несчастливое  число')
ne1=input()
ne=int(ne1)
i=0
slog3=[]
aa=0
ss=0
slog11=[]
slog22=[]
print('chi=',chi)
slog1=0
slog2=0
ww=1
def recur(chi):
     global aa
     global i
     global ss
     global slog11
     global slog22
     #slog1=0
     #slog2=0
     global slog1
     global slog2
     global ww
     dd=0
     ff=0
   
   
     global slog3           
   
     #pdb.set_trace()
     if ne==3:
       #if i==1:  
         if slog1==6:
            
               slog3.append('4')
               slog3.append('2')
               
               i=1
               print('slog3=',slog3)
         elif slog1==5:
         
           # print('ss=',ss)
           # dd=ss-2
            #ff=2**dd
            #while ff!=0:
               slog3.append('5')
              
             #  ff=ff-1
         
               print('slog3=',slog3)

               i=1
               print('slog3=',slog3)
         elif slog1==7:
            print("ss KKONEX=",ss)
            mm=0
            nn=0
            nn=slog11.count(slog1)
            mm=slog22.count(slog1)
            print('mm+nn=',mm+nn)
            print(slog11)
            print(slog22)
            #dd=ss-2
            #ff=2**dd
            ff=mm+nn
            while ff!=0:
               slog3.append('5')
               slog3.append('2')
               ff=ff-1
         
            i=1  
            print('slog3=',slog3)
         
         elif slog1==9:
            dd=ss-2
            ff=2**dd
            while ff!=0:
               slog3.append('5')
               slog3.append('4')
               ff=ff-1
            i=1
            print('slog3=',slog3)
         elif slog1==4:
          if slog1==slog2: dd=ss
          else:   dd=ss-1
        
          ff=2**dd
          while ff!=0:
             slog3.append('4')
             ff=ff-1
          i=1
          print('slog3=',slog3)
         else:
           if chi%2==0:
             slog1=chi/2
             ss=ss+1
             print('ss nach=',ss)
             slog2=slog1
             if i!=1:
               print('i=',i)   
               slog11.append(slog1)
               slog22.append(slog2)
               print('chi=',chi)
               print('slog1=',slog1)
               print('slog2=',slog2)
              
             recur(slog1)
           else:
              chi=chi+1
              slog1=chi/2
              ss=ss+1
              slog2=chi-1-slog1
              if i!=1:
                print('i=',i)   
                slog11.append(slog1)
                slog22.append(slog2)
                recur(slog1)
                print('chi=',chi)
              
                print('slog1=',slog1)
                print('slog2=',slog2)
              
              
              if slog2>3:
                  lnn=len(slog22)   
                  print('lnn=',lnn)
                  print('ww=',ww)
                  print('slog11=',slog11)
                  print('slog22=',slog22)
                  
                  if i==1:
                     
                      
                       if lnn>ww:
                                        
                            slog1=slog22[lnn-ww] #поднимаемся наверх по дереву
                            print('новый slog1однимаемся по дереву=',slog1)
                           
                         
                       if lnn-ww==0:
                           # slog11=[]
                            
                            slog1=slog22[lnn-ww]
                            slog11=[]
                            slog22=[]
                            print('вторая ветка',slog22)
                            slog22.append(slog1)
                            print('вторая ветка новая',slog22)
                       ww=ww+1    
                  else:   slog1=slog2
                  print('slog1=',slog1)
                  recur(slog1)
              else:
                slog3.append(slog1)
                slog3.append(slog2)
                i=1 
         
recur(chi)
print(slog3)
print(slog11)
print(slog22)
