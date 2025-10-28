import psycopg2

conn = psycopg2.connect("dbname=suppliers user=duy password=123456")
print("Connected successfully!")
conn.close()
