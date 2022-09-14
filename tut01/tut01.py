import pandas as pd
import csv
try:
  dataset=pd.read_csv(r"octant_input.csv")
  val=dataset.values
  val1=val.tolist()
except:
  print("file is not found")
try:
  u=dataset['U'].values
  Uavg=0
  count=0
  for i in u:
    Uavg=Uavg+i
    count=count+1
  Uavg=Uavg/count
  v=dataset['V'].values
  Vavg=0
  count1=0
  for i in v:
    Vavg=Vavg+i
    count1=count1+1
  Vavg=Vavg/count1
  w=dataset['W'].values
  Wavg=0
  count2=0
  for i in w:
    Wavg=Wavg+i
    count2=count2+1
  Wavg=Wavg/count2
except:
  print("there is typo in average calculation")
df=[Uavg,Vavg,Wavg]
ls=[]
for i in range(0,29745):
  ls.append([val1[i][0],val1[i][1]-Uavg,val1[i][2]-Vavg,val1[i][3]-Wavg])
for i in range(0,29745):
  if(ls[i][1]>=0):
    if(ls[i][2]>=0):
      if(ls[i][3]>=0):
        ls[i].append(1)
      else:
        ls[i].append(-1)
    else:
      if(ls[i][3]>=0):
        ls[i].append(4)
      else:
        ls[i].append(-4)
  else:
    if(ls[i][2]>=0):
      if(ls[i][3]>=0):
        ls[i].append(2)
      else:
        ls[i].append(-2)
    else:
      if(ls[i][3]>=0):
        ls[i].append(3)
      else:
        ls[i].append(-3)
lsdf=pd.DataFrame(ls,columns=['Time',"U'","V'","W'",'Octant'])
dic={'1':0,'-1':0,'2':0,'-2':0,'3':0,'-3':0,'4':0,'-4':0}