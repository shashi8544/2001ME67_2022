
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

import os
from datetime import datetime

start_time = datetime.now()
    ##### importing pandas
try:
  import pandas as pd
except:
  print("There is error in importing pandas!!!!!!!! Pleaase install Pandas!!!!!!")
  exit()
def isvalid(times):
    ans=False
    x=check_date(times.split(" ")[0])
    z2=times.split(' ')[1]
    if(z2[1]!=" "):
        z1=z2
    else:
        z1=times.split(' ')[2]
    t1=int(z1[0])
    t1=t1*10+int(z1[1])
    t2=int(z1[3])
    t2=t2*10+int(z1[4])
    if(x==0 or x==3):
        if(t1==14 or (t1==15 and t2==0)):
            ans=True
    return ans
def check_date(dat):
    try:
        x=dat
        t=(x[3])
        t+=(x[4])
        t+=(x[5])
        t+=(x[0])
        t+=(x[1])
        t+=(x[2])
        t+=(x[6])
        t+=(x[7])
        t+=(x[8])
        t+=(x[9])
        d = pd.Timestamp(t)
        return d.dayofweek
    except:
        print("Either there is error in date format or in function!!!!!!!!!")
        exit()
def attendance_report():
    try:
        input_attendance=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\tt\input_attendance.csv')
        total_student=pd.read_csv(r'C:\Users\DELL\OneDrive\Desktop\tt\input_registered_students.csv')
    except:
        print("there is error in uploading attendance file and total student file")
        exit()
        
    
    #### creating series of roll no and name and unique time-stamp
    try:
        Roll_list=total_student['Roll No'].to_list()
        Name_list=total_student['Name'].to_list()
        list1=[]
        list_timest=(input_attendance['Timestamp']).to_list()
        list_attend=(input_attendance['Attendance']).to_list()
        for items in input_attendance['Timestamp']:
            z=items.split(' ')[0]
            x=check_date(z)
            if(x==0 or x==3):
                list1.append(items)                        
    except:
        print("There is some error in creating name list")
        exit()  
    try:
        total_lec=0
        total_lec_date=[]
        init="333"
        for i in range(len(list1)):
          if(list1[i].split(" ")[0]!=init):
              total_lec=total_lec+1
              total_lec_date.append(list1[i].split(" ")[0])
              init=list1[i].split(" ")[0]
    except:
        print("error in calculating total lecture taken")

attendance_report()
#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))