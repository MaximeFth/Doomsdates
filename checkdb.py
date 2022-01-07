import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("MyScores.db")
df = pd.read_sql_query("SELECT * from scores", con)

# Verify that result of SQL query is stored in the dataframe
print(df)

con.close()