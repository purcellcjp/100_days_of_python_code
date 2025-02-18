import pandas as pd

student_dict = {
    'student':['Me','Myself','I'],
    'score':[56,79,98]
}

df = pd.DataFrame(student_dict)

# print(df.head())

# Loop dataframe
# for (key, value) in df.items():
#     print(key,value)

# better method is to use iterrows
for (index,row) in df.iterrows():
    # print(row.student, row.score)
    if row.student == 'Me':
        print(row.score)