import csv
import sqlite3

csv_file_path = 'data/FamilyTree.csv'

conn = sqlite3.connect('data/FamilyTree.db')
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Family TEXT,
    Year INTEGER,
    Major TEXT,
    Minor TEXT,
    LinkedIn TEXT
);
'''
cursor.execute(create_table_query)

with open(csv_file_path, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        insert_query = '''
        INSERT INTO students (Name, Family, Year, Major, Minor, LinkedIn)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(insert_query, (row['Name'], row['Family'], row['Year'], row['Major'], row['Minor'], row['LinkedIn']))

conn.commit()
conn.close()

print("data inserted into db!")
