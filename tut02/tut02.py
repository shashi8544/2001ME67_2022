
mod=5000
from cmath import nan
import openpyxl

wb = openpyxl.load_workbook(r'C:\Users\DELL\OneDrive\Desktop\temp_octant\input_octant_transition_identify_Copy.xlsx')

sheet = wb.active
Uavg=0
Vavg=0
Wavg=0
ls=[]
for row in sheet.iter_rows(min_row=1, min_col=1, max_row=29746, max_col=4):
    lst1=[]
    for cell in row:
        lst1.append(cell.value)
    ls.append(lst1)
for i in range(1,29746):
    Uavg=Uavg+ls[i][1]
    Vavg=Vavg+ls[i][2]
    Wavg=Wavg+ls[i][3]
Uavg=Uavg/29745
Vavg=Vavg/29745
Wavg=Wavg/29745

lst_avg=[["Uavg","Vavg","Wavg"],[Uavg,Vavg,Wavg]]
i=0
for row in sheet.iter_rows(min_row=1, min_col=5, max_row=2, max_col=7):
    j=0
    for cell in row:
        cell.value=lst_avg[i][j]
        j=j+1
    i=i+1
lst_newval=[]
for i in range(1,29746):
    lst_newval.append([ls[i][1]-Uavg,ls[i][2]-Vavg,ls[i][3]-Wavg])
sheet.cell(row=1,column=8).value="Uavg'"
sheet.cell(row=1,column=9).value="Vavg'"
sheet.cell(row=1,column=10).value="Wavg'"    
sheet.cell(row=1,column=11).value="Octant"    

i=0
for row in sheet.iter_rows(min_row=2, min_col=8, max_row=29746, max_col=10):
    j=0
    for cell in row:
        cell.value=lst_newval[i][j]
        j=j+1
    i=i+1

lst_octant = []
for p in lst_newval:
    if(p[0]>=0):
        if(p[1]>=0):
            if(p[2]>=0):
                lst_octant.append(1)
            else:
                lst_octant.append(-1)
        else:
            if(p[2]>=0):
                lst_octant.append(4)
            else:
                lst_octant.append(-4)
    else:
        if(p[1]>=0):
            if(p[2]>=0):
                lst_octant.append(2)
            else:
                lst_octant.append(-2)
        else:
            if(p[2]>=0):
                lst_octant.append(3)
            else:
                lst_octant.append(-3)

i=0
for row in sheet.iter_rows(min_row=2, min_col=11, max_row=29746, max_col=11):
    for cell in row:
        cell.value=lst_octant[i]
    i=i+1

t=0
if(29746%mod==0):
    t=29746//mod
else:
    t=(29746//mod)+1
wb.save(r'C:\Users\DELL\OneDrive\Desktop\temp_octant\input_octant_transition_identify_Copy.xlsx')