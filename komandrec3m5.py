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
     dd=0
     ff=0
   
   
     global slog3           
   
     pdb.set_trace()
     if ne==3:
       #if i==1:  
         if slog1==6:
            dd=ss-1
            ff=2**dd
            while ff!=0:
               slog3.append('4')
               slog3.append('2')
               ff=ff-1
            i=1
         elif slog1==5:
         
            print('ss=',ss)
            dd=ss
            ff=2**dd
            while ff!=0:
               slog3.append('5')
               slog3.append('2')
               ff=ff-1
         
            
            i=1
         elif slog1==7:
            print("ss KKONEX=",ss)
            dd=ss-1
            ff=2**dd
            while ff!=0:
               slog3.append('5')
               slog3.append('2')
               ff=ff-1
         
            i=1  
         elif slog1==8:
       
          
            dd=ss
            ff=2**dd
            while ff!=0:
               slog3.append('4')
           
               ff=ff-1
         
          
            i=1
         
         elif slog1==9:
            dd=ss-1
            ff=2**dd
            while ff!=0:
               slog3.append('5')
               slog3.append('4')
               ff=ff-1
            i=1
         elif slog1==4:
          
          dd=ss
          ff=2**dd
          while ff!=0:
             slog3.append('4')
             ff=ff-1
          i=1
     
         else:
           if chi%2==0:
             slog1=chi/2
             ss=ss+1
             print('ss nach=',ss)
             slog2=slog1
             slog11.append(slog1)
             slog22.append(slog2)
             recur(slog1)
           else:
              chi=chi+1
              slog1=chi/2
              ss=ss+1
              slog2=chi-1-slog1
              slog11.append(slog1)
              slog22.append(slog2)
              recur(slog1)
              print('slog2nech=',slog2)
              
            
              if slog2>3:
                   slog1=slog2
                   recur(slog1)
              else:
                slog3.append(slog1)
                slog3.append(slog2)
                i=1 
         
recur(chi)
print(slog3)
