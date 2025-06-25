import mysql.connector

# Connect to your MySQL DB
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='merico',
    password='merico',
    database='lake'
)
cursor = conn.cursor()

# Step 1: Find all tables with the column _raw_data_table
cursor.execute("""
    SELECT table_name
    FROM information_schema.columns
    WHERE column_name = '_raw_data_table'
      AND table_schema = %s
""", ('lake',))
tables = cursor.fetchall()

matching_tables = []

# Step 2: Check each table for the value 'gitextractor'
for (table,) in tables:
    try:
        query = f"SELECT 1 FROM `{table}` WHERE `_raw_data_table` = 'gitextractor' LIMIT 1"
        cursor.execute(query)
        if cursor.fetchone():
            matching_tables.append(table)
    except mysql.connector.Error:
        # Skip tables that cause errors
        continue

# Output
print("Matching tables:")
for table in matching_tables:
    print(table)

cursor.close()
conn.close()
