import pymysql.cursors

db = pymysql.connect(host="127.0.0.1", database="bugtracker", user="root", password="")


try:
    cursor = db.cursor()
    cursor.execute("select * from mantis_project_table")
    for row in cursor.fetchall():
            print(row)
finally:
    db.close()