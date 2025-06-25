import mysql.connector

# MySQL connection info — edit these!
# fourth branch comment
config = {
    'user': 'merico',
    'password': 'merico',
    'host': '127.0.0.1',
    'database': 'lake',
}

# Table name to skip
skip_table_name = '_devlake_locking_stub'

def main():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    print(f"Fetching table list from database `{config['database']}`...")
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = %s AND table_type = 'BASE TABLE';
    """, (config['database'],))
    tables = cursor.fetchall()
    print(f"Found {len(tables)} tables.")

    non_empty_tables = []
    total_tables = len(tables)

    for idx, (table_name,) in enumerate(tables, start=1):
        if table_name == skip_table_name:
            print(f"[{idx}/{total_tables}] Skipping table `{table_name}` as requested.")
            continue

        print(f"[{idx}/{total_tables}] Checking table `{table_name}`...")
        cursor.execute(f"SELECT EXISTS(SELECT 1 FROM `{table_name}` LIMIT 1);")
        has_rows = cursor.fetchone()[0]
        if has_rows:
            print(f"--> Table `{table_name}` has rows.")
            non_empty_tables.append(table_name)
        else:
            print(f"--> Table `{table_name}` is empty.")

    print("\nTables with at least one row (excluding skipped):")
    for t in non_empty_tables:
        print(f"- {t}")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
