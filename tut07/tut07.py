

###### define mod value
mod=5000


##### importing libraries
try:
    from datetime import datetime
    start_time = datetime.now()
    import os
    import glob
    import pandas as pd
    from cmath import nan
    import openpyxl
    from openpyxl.styles import Border, Side
    from openpyxl.styles import PatternFill
except:
    print("there is some error in importing libraries check whether all libraries is installed or not")
    exit()

#### checking python version
try:
    from platform import python_version
    ver = python_version()

    if ver == "3.8.10":
        print("Correct Version Installed")
    else:
        print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
except:
    print("please install platform libraries")


######## Reading excel input file
try:
    os.chdir(r"C:\Users\DELL\OneDrive\Desktop\tt\tut07\input")
    extension='xlsx'
    all_filesname = [i for i in glob.glob('*.{}'.format(extension))]
except:
    print("there is some error in reading excel file!!!!!!!!! Please check ")
