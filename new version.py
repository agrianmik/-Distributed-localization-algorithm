#1
import pandas as pd
import numpy as np
import csv
import math
import matplotlib.pyplot as plt
#from shapely.geometry.polygon import Polygon

#2
data_file='t2.6x6.e2.m45.csv'
data=pd.read_csv(data_file)

#4
data

#5
mydata=[]
with open(data_file) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    line_count=0
    for row in csv_reader:
       mydata.append(row)
       
#6
myx=[]
myy=[]
for each in range(len(mydata[0])):
    x=mydata[0][each][7:10]
    #if (mydata[0][each][14])==':':
    y=mydata[0][each][13:16]
    
    if (mydata[0][each][13])==':':
        y=mydata[0][each][14:17]
    
    if (mydata[0][each][13])=='y':
        y=mydata[0][each][15:18]
    
    #else:
    #y=float(mydata[0][each][14:16])
    #if y==12.0:
        #y=120.0
    #elif y==15.0:
        #y=150
              
    myx.append(x)
    myy.append(y)
    
#7
length=len(myx)
dim=(2,length)
device_position=np.zeros(dim)

#8
device_position[0,:]=myx
device_position[1,:]=myy

#9
device_position

#10
plt.scatter(myx,myy)
plt.title('Sensor position in grid')

#11
distance measurement

#12
D=np.array(mydata)

#13
D=D[1:,:]

#14
D
#15
norm_count=len(myx); #total number of the localize devices

#16
def get_d(device_position,n1,n2):
   
#calculate the eclidian minimum distance between two point
            #device1=device_position[:,n1]
            #device2=device_position[:,n2]
        
           
            distance=float(D[n2-1,n1-1])
            #if distance==-1:
                #distance=30
               #distance=math.sqrt((y[n2-1]-y[n1-1])**2+(x[n2-1]-x[n1-1])**2)
            return distance
        
#17
def reboust(a,b,c):
           
#set the threshold to be 45 
           reboust_thresh=(45*3.142)/180
 
#determine the side having the minimum distance
           if ((a<=b) and (a<=c)):
               minvalue=a
               d=b
               e=c
           elif (b<=a and b<=c):
               minvalue=b
               d=a
               e=c
           else:
               minvalue=c
               d=a
               e=b


#check with the minimum distance 
           costh=(d**2+e**2-minvalue**2)/(2*d*e)

#if it is not reboust then return 0
#if it is reboust then return 1

           if (minvalue*(1-(costh)**2) < reboust_thresh):
    
              check=0
           else: 
              check=1
    
           return check
        
#18
length=100
dim=(length,4)
Quadsi=np.zeros(dim)
i=0
count=1
for j in range(1,norm_count+1):
    dij=get_d(device_position,i,j) #get the distance between node i and j
    
    #if there is no distance between i and j, then continue
    if (dij==-1):
        continue
    
   
    for k in range(1,norm_count):
          djk=get_d(device_position,j,k) #get distance between j and k
          dik=get_d(device_position,i,k) #get distance between i and k
          
          if (k==j or djk==-1 or dik==-1):
           continue
          
            
          
          if(reboust(dij,dik,djk)==0): #check if dij,dik,djk is reboust else continue
            
               continue
               
        
           
          for l in range(1,norm_count+1):
               dkl=get_d(device_position,k,l);

               if (l==k or l==j or dkl==-1):
                   continue

              
               dlj=get_d(device_position,l,j)
            
               if (dlj==-1) or (dlj==-1):  #if there is no distance between l and j, then continue
                   continue

             
               dil=get_d(device_position,i,l)
               if (dil==-1):  #if there is no distance between i and l, then continue
                   continue


               #then check if all distance are reboust
               
               if (reboust(djk,dkl,dlj)==1 & reboust(dij,dil,dlj)==1 & reboust(dik,dil,dkl)==1):

          #add reboust nodes to the Quadsi
                  d=[i,j,k,l]
                  print(d)
                  d=[int(x) for x in d]
                  Quadsi[count,:]=d  
                  count=count+1
                  
#19
for each in range(len(Quadsi)):
        
         
         xq=[int(x) for x in Quadsi[each]]
         
         xx=device_position[0,xq]
         yy=device_position[1,xq]
         plt.scatter(xx,yy)
         
         for c in range(len(xx)):
            s=str(xq[c])
            s='  s'+s
            plt.text(xx[c],yy[c],s,fontsize=10,fontweight='light')
         #plt.hold(True)
            
#plt.show()     
#3
#3
#3
#3
#3
#3
#3
