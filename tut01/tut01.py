#importing pandas which manage dataframe
import pandas as pd


#try reading input file if present in curr directory

try:
  dataset=pd.read_csv(r"octant_input.csv")
  val=dataset.values
  val1=val.tolist()
except:
  print("file is not found")


#calculating average of u v and w from given dataset

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


#from csv creating a list of u',v',w'

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


#creating dataframe of octant and calculating overall count of octant values 

try:
  lsdf=pd.DataFrame(ls,columns=['Time',"U'","V'","W'",'Octant'])
  dic={'1':0,'-1':0,'2':0,'-2':0,'3':0,'-3':0,'4':0,'-4':0}
  for i in range(29745):
    dic[str(ls[i][4])]=dic[str(ls[i][4])]+1
except:
  print("ls is not computed correctly")


#taking user input(mod value)

mod=5000


#calculating range of mod and its count value

ans=[]
t=30000//mod
temp=[]
y=0
for i in range(t):
  x=mod*i
  if(i==t-1):
    y=27944
  else:
    y=mod*(i+1)-1
  z=str(x)+'-'+str(y)
  temp.append(z)
  dic1={'1':0,'-1':0,'2':0,'-2':0,'3':0,'-3':0,'4':0,'-4':0}
  for j in range(x,y):
    dic1[str(ls[j][4])]=dic1[str(ls[j][4])]+1
  temp1=[dic1['1'],dic1['-1'],dic1['2'],dic1['-2'],dic1['3'],dic1['-3'],dic1['4'],dic1['-4']]
  dic2={z:temp1}
  ans.append(dic2)

#updating dataset to generate output file 


dataset['U avg']=''
dataset['V avg']=''
dataset['W avg']=''

dataset['U avg'][0]=df[0]
dataset['V avg'][0]=df[1]
dataset['W avg'][0]=df[2]

dataset=dataset.join([lsdf["U'"],lsdf["V'"],lsdf["W'"],lsdf["Octant"]])
dataset['']=''
dataset[''][1]='User Input'
dataset['Octant ID']=''
dataset['Octant ID'][0]='Overall Count'
dataset['Octant ID'][1]='MOD '+str(mod)
dataset['1']=''
dataset['-1']=''
dataset['2']=''
dataset['-2']=''
dataset['3']=''
dataset['-3']=''
dataset['4']=''
dataset['-4']=''
for i in range(len(temp)):
  dataset['Octant ID'][i+2]=temp[i]
dataset.head(10)
clist=list(dataset.columns)[-8:]
for i in range(len(dic)):
  dataset[clist[i]][0]=list(dic.values())[i]
for row in range(len(ans)):
  for col in range(len(clist)):
    dataset[clist[col]][row+2]=list((ans[row].values()))[0][col]
dataset.to_csv(r'Octant_output.csv',index=False)