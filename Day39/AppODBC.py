import pyodbc
import pandas as pd


# Connection string
conn_str = (
    "Driver={SQL Server};"
    "Server=DESKTOP-848TND6;"
    "Database=AdventureWorks2022;"
    "Trusted_Connection=yes;"

)

# Create connection
conn = pyodbc.connect(conn_str)

query = """
select LoginID,
JobTitle,
BirthDate,
MaritalStatus
from HumanResources.Employee
where (Gender = 'F')
"""

cursor = conn.cursor()
# Execute query
cursor.execute(query)
rows = cursor.fetchall()
# print(rows)
df = pd.read_sql_query(query, conn)

print(df.head())

conn.close()
