import pandas as pd
from datetime import datetime

df = pd.DataFrame([[1, 'Alex', 'Smur', 21, 'Python Developer', datetime.fromisoformat('2022-01-01T09:45:12')],
[2,'Justin', 'Forman', 25, 'Java Developer',datetime.fromisoformat('2022-01-01T11:50:25')],
[3,'Set', 'Carey', 35, 'Project Manager', datetime.fromisoformat('2022-01-01T10:00:45')],
[4,'Carlos', 'Carey', 40, 'Enterprise architect', datetime.fromisoformat('2022-01-01T09:07:36')],
[5,'Gareth', 'Chapman', 19, 'Python Developer', datetime.fromisoformat('2022-01-01T11:54:10')],
[6,'John', 'James', 27, 'IOS Developer', datetime.fromisoformat('2022-01-01T09:56:40')],
[7,'Bob', 'James', 25, 'Python Developer', datetime.fromisoformat('2022-01-01T09:52:45')]],
columns=['Id', 'Name', 'Surname', 'Age', 'Job', 'Datetime'])

print(df)