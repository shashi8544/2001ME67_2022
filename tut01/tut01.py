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