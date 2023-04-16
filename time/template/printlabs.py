import mysql.connector as c
con = c.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
query = "select * from time"
cursor = con.cursor()
cursor.execute(query)
records = cursor.fetchall()
table = ['Day', '1', '2', '3', '4', '5', '6', '7', '8']
week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
c = 0
goal = input()
f = 0
while c < (len(records)):
    data_items = []
    if records[c][0][:len(records[c][0]) - 4].lower() == goal:
        f = 1
        for i in range(6):
            x = []
            x.extend(records[c][1:])
            data_items.append(x)
            c += 1
        format_row = "{:>9}" * (len(table) + 1)
        print(format_row.format("", *table))
        for team, row in zip(table, data_items):
            print(format_row.format(team, *row))
        print("...........................................................")
    else:
        c += 1
        continue 
if f == 0:
    print("No period assigned")

