import pymssql

conn = pymssql.connect(
    server='DESKTOP-848TND6',
    user= 'sa',
    password='Valkyrie!Th0r69',
    database='AdventureWorks2022',
    as_dict=True,
)

query = """
select LoginID,
JobTitle,
BirthDate,
MaritalStatus
from HumanResources.Employee
where (Gender = 'F')
"""

cursor = conn.cursor()
cursor.execute(query)

records = cursor.fetchall()
for row in records:
    print(f"{row.LoginID}|{row.JobTitle}")

cursor.close()
conn.close()
