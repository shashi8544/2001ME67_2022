
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
        input_attendance=pd.read_csv(r'C:\Users\DELL\OneDrive\Documents\GitHub\2001ME67_2022\tut06\input_attendance.csv')
        total_student=pd.read_csv(r'C:\Users\DELL\OneDrive\Documents\GitHub\2001ME67_2022\tut06\input_registered_students.csv')
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

#### creating individual report
    try:
        lent=len(list_timest)
        
        list_fin=["","","","","","","",""]
        columnss=["Date","Roll","Name","Total Attendance Count","Real","duplicate","Invalid","Absent"]
        list_roll=[]
        for k in range(len(Roll_list)):
            list_fin=["","","","","","","",""]
            list_fin[1]=Roll_list[k]
            list_fin[2]=Name_list[k]
            list_roll.append(list_fin)
            list_fin=["","","","","","","",""]
            for j in range(len(total_lec_date)):
                list_fin[0]=total_lec_date[j]
                date_init=total_lec_date[j]
                total_attendance_count=0
                invalid=0
                for i in range(lent):
                    if(list_attend[i]==None):
                        continue
                    curr_roll=list_attend[i].split(" ")[0]
                    if(curr_roll==Roll_list[k]):
                        curr_date=list_timest[i].split(" ")[0]         
                        curr_time=list_timest[i].split(" ")[1]
                        if(date_init!=curr_date):
                            continue        
                        t1=curr_time[0]
                        t1=t1+curr_time[1]
                        t2=curr_time[3]
                        t2=t2+curr_time[4]
                        if(t1=="14" or (t1=="15" and t2=="00")):
                            total_attendance_count=total_attendance_count+1
                            
                        else:
                            invalid=invalid+1
                list_fin[3]=total_attendance_count
                if(total_attendance_count>0):
                    list_fin[4]=1
                else:
                    list_fin[4]=0
                if(total_attendance_count>0):
                    list_fin[5]=total_attendance_count-1
                else:
                    list_fin[5]=0
                list_fin[6]=invalid
                if(total_attendance_count==0):
                    list_fin[7]=1
                else:
                    list_fin[7]=0
                list_roll.append(list_fin)
                list_fin=["","","","","","","",""]
            df1=pd.DataFrame(list_roll,columns=columnss)
            columnss=["Date","Roll","Name","Total Attendance Count","Real","duplicate","Invalid","Absent"]
            df1.to_excel(r'C:\Users\DELL\OneDrive\Documents\GitHub\2001ME67_2022\tut06\Output\{0}.xlsx'.format(Roll_list[k]),index=False)
            list_roll=[]    
    except:
        print("There is error in calculating attendence report")



    #### creating consolidate excel file
    try:
        list_ans=[]
        columns1=[]
        columns2=["(sorted by roll)",""]
        columns1.append("Roll")
        columns1.append("Name")
        for item in total_lec_date:
            columns1.append(item)
            columns2.append("")
        columns1.append("Actual Lecture Taken")
        columns1.append("Total Real")
        columns1.append("% Attendance")
        columns2[2]="Atleast one Real is P"
        columns2.append("(=Total Mon+Thru dynamic count)")
        columns2.append("")
        columns2.append("Real/Actual Lecture Taken (Keep two digits decimal precision e.g., 90.58, round off )")
        list_ans.append(columns2)
        columns2=[]
        for i in range(len(Roll_list)):
            columns2.append(Roll_list[i])
            columns2.append(Name_list[i])
            count=0
            present=False
            for j in range(len(total_lec_date)):
                for k in range(lent):
                    if(list_attend[k]==None):
                        continue
                    curr_roll=list_attend[k].split(" ")[0]
                    if(curr_roll==Roll_list[i]):
                        curr_date=list_timest[k].split(" ")[0]         
                        curr_time=list_timest[k].split(" ")[1]
                        if(total_lec_date[j]==curr_date):       
                            t1=curr_time[0]
                            t1=t1+curr_time[1]
                            t2=curr_time[3]
                            t2=t2+curr_time[4]
                            if(t1=="14" or (t1=="15" and t2=="00")):
                                present=True
                if(present==True):
                    columns2.append("P")
                    count=count+1
                else:
                    columns2.append("A")
                present=False
            columns2.append(total_lec)
            columns2.append(count)
            Attendence=count*100/total_lec
            columns2.append(round(Attendence,2))
            list_ans.append(columns2)
            columns2=[]
        df2=pd.DataFrame(list_ans,columns=columns1)
        df2.to_excel(r'C:\Users\DELL\OneDrive\Documents\GitHub\2001ME67_2022\tut06\Output\attendance_report_consolidated.xlsx',index=False)
    except:
        print("There is some error in creating consolidate file")

attendance_report()
#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
