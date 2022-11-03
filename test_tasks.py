import pandas as pd
from datetime import datetime, time

#Build dataframe
df = pd.DataFrame([[1, 'Alex', 'Smur', 21, 'Python Developer', datetime.fromisoformat('2022-01-01T09:45:12')],
[2,'Justin', 'Forman', 25, 'Java Developer',datetime.fromisoformat('2022-01-01T11:50:25')],
[3,'Set', 'Carey', 35, 'Project Manager', datetime.fromisoformat('2022-01-01T10:00:45')],
[4,'Carlos', 'Carey', 40, 'Enterprise architect', datetime.fromisoformat('2022-01-01T09:07:36')],
[5,'Gareth', 'Chapman', 19, 'Python Developer', datetime.fromisoformat('2022-01-01T11:54:10')],
[6,'John', 'James', 27, 'IOS Developer', datetime.fromisoformat('2022-01-01T09:56:40')],
[7,'Bob', 'James', 25, 'Python Developer', datetime.fromisoformat('2022-01-01T09:52:45')]],
columns=['Id', 'Name', 'Surname', 'Age', 'Job', 'Datetime'])

####################### CONDITION 1 ######################

#Create copy of df, add new column with condition 1
df_1 = df.copy()
def condition_1(data):
    if 'Developer' in data['Job'] and data['Age'] > 18 and data['Age'] <= 21:
        return time(hour=9, minute=0)
    elif 'Developer' in data['Job']:
        return time(hour=9, minute=15)

df_1['TimeToEnter'] = df_1.apply(condition_1, axis=1)
print('Condition 1:\n', df_1)

##########################################################
import pyexcelerate

#Function for transforming dataframe to excel
def dataframeToExcel(filename, df, sheet_name='Sheet1', origin=(1,1)):
    wb = pyexcelerate.Workbook()
    ws = wb.new_sheet(sheet_name)

    columns = df.columns.tolist()
    ro = origin[0]
    co = origin[1]
    ws.range((ro, co), (ro, co+len(columns))).value = [[*columns]]
    
    # Write the data
    row_num = df.shape[0]    
    col_num = df.shape[1]
    ro = origin[0]+1
    co = origin[1]
    ws.range((ro, co), (ro+row_num,co+col_num)).value = df.values.tolist()

    #Columns styling
    #Make datetime cells bigger and change their formatting
    longRawStyle = pyexcelerate.Style(size=-1)
    ws.set_col_style(5, longRawStyle)
    ws.set_col_style(6, longRawStyle)
    for i in range(ro, ro+row_num):
        ws.set_cell_style(i, 6, pyexcelerate.Style(format=pyexcelerate.Format('dd.mm.yy hh:mm')))
    ws.set_col_style(7, longRawStyle)
    for i in range(ro, ro+row_num):
        ws.set_cell_style(i, 7, pyexcelerate.Style(format=pyexcelerate.Format('hh:mm')))
    wb.save(filename)

#Transform dataframe 1 to excel
dataframeToExcel('df_1.xlsx', df_1)

####################### CONDITION 2 ######################
