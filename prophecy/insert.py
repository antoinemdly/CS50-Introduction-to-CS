from cs50 import SQL

db = SQL("sqlite:///roster.db")

rows = db.execute("SELECT * FROM students")
"""
for row in rows:
    insert_query = "INSERT INTO student (id, student_name) VALUES (:id, :student_name)"
    data_to_insert = {"id": row['id'], "student_name": row['student_name']}
    db.execute(insert_query, **data_to_insert)
"""
"""
for row in rows:
    insert_query = "INSERT INTO houses (student_id, house) VALUES (:student_id, :house)"
    data_to_insert = {"student_id": row['id'], "house": row['house']}
    db.execute(insert_query, **data_to_insert)
"""

for row in rows:
    insert_query = "INSERT INTO heads (head_house, head) VALUES (:head_house, :head)"
    data_to_insert = {"head_house": row['house'], "head": row['head']}
    db.execute(insert_query, **data_to_insert)
