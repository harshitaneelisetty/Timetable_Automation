from flask import Flask,render_template,request
from prettytable import PrettyTable
import mysql.connector as c1234
import random
import webbrowser
class Solution:
    name = ""
    Name = ''
    dept = ''
    email = ''
    deg = ''
    pre1 = ''
    pre2 = ''
    pre3 = ''
    pre4 = ''
    namead = ""
    deptad = ""
    emailad = ""
    degad = ""

global c1
c1 = Solution()
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

#I - I
# a11
@app.route('/a11')
def a11():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time3"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'ICSEA':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <h3> I-I CSE-A TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo31.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


 #b11   
@app.route('/b11')
def b11():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time3"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'ICSEB':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> I-I CSE-B TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo32.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


#c11
@app.route('/c11')
def c11():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time3"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'ICSEC':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> I-I CSE-C TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo33.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


# I - II
#a12
@app.route('/a12')
def a12():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time4"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'ICSEA':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> I-II CSE-A TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo34.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


#b12
@app.route('/b12')
def b12():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time4"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'ICSEB':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> I-II CSE-B TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo35.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


#c12
@app.route('/c12')
def c12():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time4"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'ICSEC':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> I-II CSE-C TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo36.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


#II - I
# a21
@app.route('/a21')
def a21():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time3"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'IICSEA':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> II-I CSE-A TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo37.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


 #b21   
@app.route('/b21')
def b21():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time3"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'IICSEB':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> II-I CSE-B TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo38.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


#c21
@app.route('/c21')
def c21():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time3"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'IICSEC':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> II-I CSE-C TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo39.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')

#II - II
# a22
@app.route('/a22')
def a22():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time4"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'IICSEA':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> II-II CSE-A TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo40.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


 #b22   
@app.route('/b22')
def b22():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time4"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'IICSEB':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> II-II CSE-B TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo41.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


#c22
@app.route('/c22')
def c22():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time4"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'IICSEC':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> II-II CSE-C TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo42.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')



#III - I
# a31
@app.route('/a31')
def a31():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time3"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'IIICSEA':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> III-I CSE-A TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo43.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


 #b31   
@app.route('/b31')
def b31():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time3"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'IIICSEB':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> III-I CSE-B TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo44.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


#c31
@app.route('/c31')
def c31():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time3"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    ans = []
    answer1 = ['.'] * 4
    c2 = 0
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0] == 'IIICSEC':
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <br>
            <h3> III-I CSE-C TIME-TABLE </h3>
            <table border = 1>
            %s
            </table>
            <br><br>
            
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0])
    filename = 'demo45.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')





@app.route('/grantpermission', methods=['POST'])
def grantpermission():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    name1 = request.form['name1']
    query = "select * from faculty"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    for i in records:
        if i[0] == name1:
            break 
    mySql_insert_query ="INSERT INTO admin VALUES ('{}', '{}','{}', '{}','{}','{}')".format(i[0], i[1], i[2], i[3], i[4], i[5])
    cursor.execute(mySql_insert_query)
    con.commit()
    v = 'Have a nice day !'
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from admin"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    query1 = "select * from time3his"
    cursor1 = con.cursor()
    cursor1.execute(query1)
    records1 = cursor.fetchall()
    if len(records1) == 54 * 3:
        v = "Danger! Time tables are going to be deleted. please save!"
    c1.name = name1
    for row in records:
        if row[0] == name1:
            #print(row)
            name = row[2]
            dept = row[3]
            email = row[4]
            deg = row[5]
            query1 = "select * from admin"
            cursor1 = con.cursor()
            cursor1.execute(query1)
            records1 = cursor.fetchall()
            for row1 in records1:
                if row1[0] == name1:
                   # print(row1)
                    c1.Name = name
                    c1.dept = dept
                    c1.email = email 
                    c1.deg = deg 
                    return render_template('permissiongranted.html', n1 = c1.namead, d1 = c1.deptad, e = c1.emailad, d = c1.degad, v1 = v)
            else:
                    c1.Name = name
                    c1.dept = dept
                    c1.email = email 
                    c1.deg = deg 
                    c1.pre1 = p1 
                    c1.pre2 = p2 
                    c1.pre3 = p3 
                    c1.pre4 = p4 
                    return render_template('permissiongranted.html', n1 = c1.namead, d1 = c1.deptad, e = c1.emailad, d = c1.degad, p1 = "please fill preferences", p2 = "please fill preferences", p3 = "please fill preferences", p4 = "please fill preferences", v1 = v)

    else:
        return render_template('permissiongranted.html')
   


@app.route('/permission')
def permission():
    return render_template('permission.html')

@app.route('/validateadmin', methods = ['POST'])
def validateadmin():
    v = 'Have a nice day !'
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from admin"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    query1 = "select * from time3his"
    cursor1 = con.cursor()
    cursor1.execute(query1)
    records1 = cursor.fetchall()
    if len(records1) == 54 * 3:
        v = "Danger! Time tables are going to be deleted. please save!"
    name1 = request.form['uname']
    c1.name = name1
    password1 = request.form['pwd2']
    for row in records:
        if row[0] == name1 and row[1] == password1:
            #print(row)
            name = row[2]
            dept = row[3]
            email = row[4]
            deg = row[5]
            c1.namead = name
            c1.deptad = dept 
            c1.emailad = email 
            c1.degad = deg
            query1 = "select * from admin"
            cursor1 = con.cursor()
            cursor1.execute(query1)
            records1 = cursor.fetchall()
            for row1 in records1:
                if row1[0] == name1:
                   # print(row1)
                    c1.Name = name
                    c1.dept = dept
                    c1.email = email 
                    c1.deg = deg 
                    return render_template('admindash.html', n1 = name, d1 = dept, e = email, d = deg, v1 = v)
            else:
                    c1.Name = name
                    c1.dept = dept
                    c1.email = email 
                    c1.deg = deg 
                    
                    return render_template('admindash.html', n1 = name, d1 = dept, e = email, d = deg, p1 = "please fill preferences", p2 = "please fill preferences", p3 = "please fill preferences", p4 = "please fill preferences", v1 = v)

    else:
        return render_template('invalidadminlogin.html')

@app.route('/generateEvenTimeTable')
def generateEvenTimeTable():
    def generateTimeTable():
        try:
            templist = []
            fact = []
            sem1 = ["ENG1", "AP", "C", "BEE1", "M1", ["ENG1", "AP", "C"]]
            sem2 = ["BEE2", "EC", "DS", "PYTHON", "M2", ["EC", "PYTHON", "DS"]]
            sem3 = ["JAVA", "DM", "PS", "SE", "DLD", ["JAVA", "DV", "CMHW", "ARTS"]]
            sem4 = ["ENG2", "WT", "OR", "DBMS", "COA", ["WT", "DBMS", "OOAD", 'JP']]
            sem5 = ["OS", "DAA", "DMDW", "SS", "TOC", ["GD", 'IOT', 'LP', 'CD']]
            sem6 = ["CN" , "FSD" , "MP" , "DAS" , "CS"]
            totalSem = [["ENG", "AP", "C", "BEE1", "M1"], ["BEE2", "EC", "DS", "PYTHON", "M2"], ["JAVA", "DM", "PS", "SE", "DLD"], ["ENG2", "WT", "OR", "DBMS", "COA"], ["OS", "DAA", "DMDW", "SS", "TOC"], ["CN" , "FSD" , "MP" , "DAS" , "CS"]]
            faculty = [["sudha mam", 8, ["WT", "JAVA", "CN", "PYTHON"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["ramarao sir", 7, ["WT", "DLD", "DM", 'LP'], 4, [0] * 6, [0] * 6, [0] * 6],
            ["kesava sir", 8, ["WT", 'LP', "CMHW"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["darmaiah sir", 8, ["WT", 'LP', "CMHW"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["ravikiran sir", 10, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["vasubabu sir", 10, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["kameswari mam", 10, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["murthy sir", 9, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["G.ramesh babu sir", 1, ["COA", "DAA", "DLD", "GD"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["srikanth sir", 2, ["COA", "DAA", "DM",  "DV"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["prasad sir", 2, ["COA", "DAA", "DM",  "DV"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["purushothamaraju sir", 15, ["DBMS", "DMDW", "OS", "CN"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["ramachandraroa sir", 12,  ["DBMS", "DMDW", "OS", "CN"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["srihariraju sir", 12,  ["ENG1", "SS", "SS2", "ENG2"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["devi mam", 7,  ["ENG1", "SS", "SS2", "ENG2"],4,[0] * 6, [0] * 6,[0] * 6],
            ["M.ramesh babu sir",7,["DM","MP","CS", "OOAD", "IOT"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["P.Raju sir",7,["DM","MP","CS", "OOAD", "IOT"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Dharmaih sir",7,["DM","MP","CS", "OOAD", "IOT"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Kalpana mam",7,["SE","OS", "CS"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Durga mam",0,["SE","OS","CD","CS"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Archana mam",7,["SE","OS","CD","CS", "CD"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Soni mam",7,["SE","OS","CD","CS", "CD", "GD"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["V.V.R.Maheshwara Rao sir",10,["SE","OS","CD","DM"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Shalem Raju sir",9,["TOC","MP","DM","CD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Tharaka satyanaran sir",2,["TOC","MP","DM","CD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Sunil sir",8 ,["DS","PYTHON","DAA","TOC"], 4 ,[0] * 6, [0] * 6, [0] * 6, []],
            ["Gayathri mam",7,["COA","PYTHON","C","CD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Silpa mam",9,["C","SE","OS","CS"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Swathi mam",8,["C","PYTHON","DS","FSD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Seenu sir", 9, ["C", "PYTHON", "JAVA", "MC"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["Phaneendhra varma sir",2,["FSD","CS","JAVA","DAS", 'GD'], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Srinivas sir",9,["AP","EP","P1","P2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Bhramhanandam sir",8,["AP","EP","P1","P2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Jagadeesh sir",10,["EC","AC","C1","C2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Ganesh sir",10,["EC","AC","C1","C2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Arun sir",7,["ENG1","ENG2","SS","SS2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Swaroop sir",6,["BEE1","BEE2","AP","EP"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Narayana kiran sir",5,["BEE1","BEE2","AP","EP"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Kalyan sagar sir",4,["BEE1","BEE2","AP","EP"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Ramu sir",9,["DMDW","DBMS","DAS","CS"], 4 ,[0] * 6, [0] * 6,[0] * 6 , []],
            ["Ratna kumari mam",9,["DMDW","DBMS","DAS","CS", "JP", "ARTS"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []]]
            faculty = sorted(faculty, key = lambda x : x[1], reverse = True)
            week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
            count = 0
            def mainFunction(subjects, labs, sem):
            
                factDict = {}
        #labs = [0, 1, 2]
                sec1 = []
                weeks = [0,1,2,3,4,5]
                w = 0
                while weeks:
                    w += 1
                    sec2 = []
                    ranWeek = random.choice(weeks)
                    subjectIndex = [0,1,2,3,4]
                    days = [1, 2, 3, 4, 5, 6, 7, 8]
                    labDays = [2, 6]
                    if labs:
                        ranLab = random.choice(labs)
                        lab = subjects[5][ranLab]
                        labs.remove(ranLab)
                        for i in faculty:
                            if lab in i[2]:
                                if i[4].count(0) != 0 and i[3] > 3:
                                
                                    if lab in factDict.values():
            
                                        try:
                                            if factDict[i[0]] == lab:
                                                randomDay = random.choice(labDays)
                                                labDays.remove(randomDay)
                                                days.remove(randomDay)
                                                days.remove(randomDay + 1)
                                                days.remove(randomDay + 2)
                                                i[4][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                            
                                                i[3] -= 1
                                                sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                                break
                                        except:
                                            continue
                                    else:
                                        factDict[i[0]] = lab
                                        randomDay = random.choice(labDays)
                                        labDays.remove(randomDay)
                                        days.remove(randomDay)
                                        days.remove(randomDay + 1)
                                        days.remove(randomDay + 2)
                                    
                                        i[4][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                    
                                        i[3] -= 1
                                        sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                        break
                           

                                elif i[5].count(0) != 0 and i[3] >= 3:
                                    if lab in factDict.values():
                                        try:
                                            if factDict[i[0]] == lab:
                                                f = 0
                                                try:
                                                    if i[4][ranWeek][0] in labDays:
                                                        x.append(i[4][ranWeek][0])
                                                        labDays.remove(i[4][ranWeek][0])
                                                        f = 1
                                                    if i[4][ranWeek][4] in labDays:
                                                        x.append(i[4][ranWeek][4])
                                                        labDays.remove(i[4][ranWeek][4])
                            
                                                except:
                                                    if i[4][ranWeek] in [2,3,4] and 2 in labDays:
                                                        x = 2
                                                        labDays.remove(2)
                                                        f = 1 
                                                    elif i[4][ranWeek] in [8,6,7] and 6 in labDays:
                                                        x = 6
                                                        labDays.remove(6)
                                                        f = 1
                                                randomDay = random.choice(labDays)
                                            labDays.remove(randomDay)
                                            days.remove(randomDay)
                                            days.remove(randomDay + 1)
                                            days.remove(randomDay + 2)
                                       
                                            i[3] -= 1
                                            i[5][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                            sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                            if f == 1:
                                                try:
                                                    labDays.extend(x)
                                                except:
                                                    labDays.append(x)
                                            break
                                        except:
                                            continue
                                    else:
                                            factDict[i[0]] = lab
                                            f = 0
                                            try:
                                                if i[4][ranWeek][0] in labDays:
                                                    x.append(i[4][ranWeek][0])
                                                    labDays.remove(i[4][ranWeek][0])
                                                    f = 1
                                                if i[4][ranWeek][4] in labDays:
                                                    x.append(i[4][ranWeek][4])
                                                    labDays.remove(i[4][ranWeek][4])
                            
                                            except:
                                                if i[4][ranWeek] in [2,3,4] and 2 in labDays:
                                                    x = 2
                                                    labDays.remove(2)
                                                    f = 1 
                                                elif i[4][ranWeek] in [8,6,7] and 6 in labDays:
                                                    x = 6
                                                    labDays.remove(6)
                                                    f = 1
                                            randomDay = random.choice(labDays)
                                            labDays.remove(randomDay)
                                            days.remove(randomDay)
                                            days.remove(randomDay + 1)
                                            days.remove(randomDay + 2)
                                            
                                            i[3] -= 1
                                            i[5][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                            sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                            if f == 1:
                                                try:
                                                    labDays.extend(x)
                                                except:
                                                    labDays.append(x)
                            
                                            break
                                elif lab not in subjects[:6] and i[3] >= 2 and i[4].count(0) != 0 and i[5].count(0) != 0:
                                
                                    factDict[i[0]] = lab
                                    if i[4][ranWeek] == 0:
                                        pass
                                    elif i[4][ranWeek][0] in labDays:
                                        x = i[4][ranWeek][0]
                                        labDays.remove(i[4][ranWeek][0])
                                    if i[5][ranWeek] == 0:
                                        pass 
                                    elif i[5][ranWeek][0] in labDays:
                                        y = i[5][ranWeek][0]
                                        labDays.remove(i[5][ranWeek][0])
                                    randomDay = random.choice(labDays)
                                    labDays.remove(randomDay)
                                    days.remove(randomDay)
                                    days.remove(randomDay + 1)
                                    days.remove(randomDay + 2)
                                    i[3] -= 1
                                    i[6][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                    sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                    try:
                                        labDays.append(x)
                                    except:
                                        continue
                                    try:
                                        labDays.append(y)
                                    except:
                                        continue
                                else:
                                    continue       
                                
                    day = 0
       #print(days, randomDay)
                    while subjectIndex:
                   # print(days)
                        day += 1
                   # randomPeriod = random.choice(days)
                        ran = random.choice(subjectIndex)
                        subject = subjects[ran]
                        subjectIndex.remove(ran)
                        for i in faculty:
                            if subject in i[2] and i[3] >= 2:
                                if subject in factDict.values():
                                    try:
                                        if factDict[i[0]] == subject:
                                            if i[4].count(0) != 0:
                                            
                                                randomPeriod = random.choice(days)
                                        #print("Hello")
                                                if i[4][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                    i[4][ranWeek].append(randomPeriod)
                                                else:
                                           # i[4].append([randomPeriod, classes])
                                                    i[4][ranWeek] = randomPeriod
                                                sec2.append([ranWeek, i[0], randomPeriod, subject])
                                                if w == 1 and subject not in subjects[5]:
                                                    i[3] -= 1
                                                break
                                            else:
                                           # print(i[4], i[0])
                                                a = 0
                                                y = []
                                                try:
                                                    x = len(i[4][ranWeek])
                                                    a = 1 
                                                except:
                                                    x = 0
                                                    pass 
                                                if a == 1:
                                                    if (i[4][ranWeek][0] in days):
                                                        days.remove(i[4][ranWeek][0])
                                                        y.append(i[4][ranWeek][0])
                                                    if (i[4][ranWeek][1] in days):
                                                        days.remove(i[4][ranWeek][1])
                                                        y.append(i[4][ranWeek][1])
                                                    if (i[4][ranWeek][2] in days):
                                                        days.remove(i[4][ranWeek][2])
                                                        y.append(i[4][ranWeek][2])
                                                    if len(i[4][ranWeek]) >= 4 and i[4][ranWeek][3] in days:
                                                        days.remove(i[4][ranWeek][3])
                                                        y.append(i[4][ranWeek][3])
                                                else:
                                                    if i[4][ranWeek] in days:
                                                        days.remove(i[4][ranWeek])
                                                        y.append(i[4][ranWeek])
                                                randomPeriod = random.choice(days)
                                                if w == 1 and subject not in subjects[5]:
                                                    i[3] -= 1

                                                if i[5][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                    i[5][ranWeek].append(randomPeriod)
                                                else:
                                           # i[4].append([randomPeriod, classes])
                                                    i[5][ranWeek] = randomPeriod
                                        
                                                sec2.append([ranWeek, i[0], randomPeriod, subject])
                                                try:
                                                    days.extend(y)
                                                except:
                                                    days.append(y)
                                                break 

                                        
                                    except:
                                        continue
                                elif i[5].count(0) != 0:
                                    if i[0] not in factDict:
                                        factDict[i[0]] = subject
                                        if i[4].count(0) != 0:
                                    #print("Hello")
                                                randomPeriod = random.choice(days)
                                           # i[4].append([randomPeriod, classes])
                                                if i[4][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                    i[4][ranWeek].append(randomPeriod)
                                                else:
                                           # i[4].append([randomPeriod, classes])
                                                    i[4][ranWeek] = randomPeriod
                                                if w == 1 and subject not in subjects[5]:
                                                    i[3] -= 1
                                                sec2.append([ranWeek, i[0], randomPeriod, subject])
                                                break
                                        else:
                                       
                                            a = 0
                                            y = []
                                            try:
                                                x = len(i[4][ranWeek])
                                                a = 1 
                                            except:
                                                x = 0
                                                pass 
                                            if a == 1:
                                                if (i[4][ranWeek][0] in days):
                                                    days.remove(i[4][ranWeek][0])
                                                    y.append(i[4][ranWeek][0])
                                                if (i[4][ranWeek][1] in days):
                                                    days.remove(i[4][ranWeek][1])
                                                    y.append(i[4][ranWeek][1])
                                                if (i[4][ranWeek][2] in days):
                                                    days.remove(i[4][ranWeek][2])
                                                    y.append(i[4][ranWeek][2])
                                                if len(i[4][ranWeek]) >= 4 and (i[4][ranWeek][3] in days):
                                                    days.remove(i[4][ranWeek][3])
                                                    y.append(i[4][ranWeek][3])
                                            else:
                                                if i[4][ranWeek] in days:
                                                    days.remove(i[4][ranWeek])
                                                    y.append(i[4][ranWeek])
                                            randomPeriod = random.choice(days)
                                            
                                            if i[5][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                i[5][ranWeek].append(randomPeriod)
                                            else:
                                           # i[4].append([randomPeriod, classes])
                                                i[5][ranWeek] = randomPeriod
                                            if w == 1 and subject not in subjects[5]:
                                                i[3] -= 1
                                            sec2.append([ranWeek, i[0], randomPeriod, subject])
                                            try:
                                                days.extend(y)
                                            except:
                                                days.append(y)
                                            days = list(set(days))
                                            break 

                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                   # print(days, randomPeriod)
                        days.remove(randomPeriod)
                    
                    sec1.append((sec2))
        #print(sec2)
                    weeks.remove(ranWeek)
                sec1 = sorted(sec1, key = lambda x : x[0][0])
                for k, v in factDict.items():
                    for i in faculty:
                        if k == i[0]:
                            if i[6].count(0) != 6:
                                i[6].append(sem)
                            elif i[5].count(0) != 6:
                                i[5].append(sem)
                            elif i[4].count(0) != 6:
                                i[4].append(sem)
                        else:
                            continue
            #print(factDict)
           
                return sec1, factDict
            x = mainFunction(sem2, [0, 1, 2], "ICSEA")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem2, [0, 1, 2], "ICSEB")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem2, [0, 1, 2], "ICSEC")
            templist.append(x[0])
            fact.append(x[1])
        #templist.append(mainFunction(sem2, [0, 1, 2]))
            x = mainFunction(sem4, [0, 1, 2, 3], "IICSEA")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem4, [0, 1, 2, 3], "IICSEB")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem4, [0, 1, 2, 3], "IICSEC")
            templist.append(x[0])
            fact.append(x[1])
            return templist, fact, faculty, False
        except Exception as e:
           # print(e)
            return templist, fact, faculty, True

    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    
    flag = True 
    goal = "sudha mam"
    while flag:
        templist,fact, faculty, flag = generateTimeTable()

    for i in fact:
        #print(i)
        print("...................................")
    yearSec = ["ICSEA","ICSEB","ICSEC","IICSEA" ,"IICSEB","IICSEC","IIICSEA","IIICSEB","IIICSEC"]
    c = -1
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS timedicteven")
    sql = '''CREATE TABLE timetable.timedicteven (
    uname VARCHAR(45) NOT NULL,
    year VARCHAR(45) NOT NULL,
    subject VARCHAR(45) NOT NULL);
    )'''
    cursor.execute(sql)
    con.close()
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()
    for i in fact:
        c += 1
        for k, v in i.items():
            mySql_insert_query = "INSERT INTO timedicteven VALUES('"+k+"', '"+yearSec[c]+"', '"+v+"');"
            cursor.execute(mySql_insert_query)
            con.commit()
    table = ['sec', 'Day', '1', '2', '3', '4', '5', '6', '7', '8']
#print(templist)
    yearSec = ["ICSEA","ICSEB","ICSEC","IICSEA" ,"IICSEB","IICSEC","IIICSEA","IIICSEB","IIICSEC"]
    c = -1
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS time4")
    sql ='''CREATE TABLE timetable.time4 (
    sec VARCHAR(45) NOT NULL,
    day VARCHAR(45) NOT NULL,
    p1 VARCHAR(45) NOT NULL,
    p2 VARCHAR(45) NOT NULL,
    p3 VARCHAR(45) NOT NULL,
    p4 VARCHAR(45) NOT NULL,
    p5 VARCHAR(45) NOT NULL,
    p6 VARCHAR(45) NOT NULL,
    p7 VARCHAR(45) NOT NULL,
    p8 VARCHAR(45) NOT NULL);
    )'''
    cursor.execute(sql)
    con.close()
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()
    for sec1 in templist:
            c += 1
            week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
    #print("          1        2         3       4        5           6          7          8")
            data_items = []
        #print(c, len(fact), len(templist))
            fact1 = fact[templist.index(sec1)]
            #print("..............................." + yearSec[c] + "............................")
        #print(fact1)
            for w in range(6):
                x = []
                x.append(yearSec[c])
                #x.append(p)
                x.append(week[w])
                for j in range(8):
                    for k in sec1[w]:
                        k = k[1:]
                        try:
                            if j + 1 in k[1]:
                                if len(k[1]) == 3:
                                    x.append(k[2] + "lab")
                            #print(k[2], end = "lab     ")
                                    break
                        except:
                            if j + 1 == k[1]:
                                x.append(k[2])
                                break
                            else:
                                continue
                    else:
                        x.append("----")
                data_items.append(x)
                mySql_insert_query = "INSERT INTO time4 VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
                cursor.execute(mySql_insert_query)
                con.commit()
                query = "select * from time4his"
                cursor = con.cursor()
                cursor.execute(query)
                records = cursor.fetchall()
                if len(records) == 36 * 3:
                    cursor = con.cursor()
                    cursor.execute("DROP TABLE IF EXISTS time4his")
                    sql ='''CREATE TABLE timetable.time4his (
                    sec VARCHAR(45) NOT NULL,
                        day VARCHAR(45) NOT NULL,
                        p1 VARCHAR(45) NOT NULL,
                        p2 VARCHAR(45) NOT NULL,
                        p3 VARCHAR(45) NOT NULL,
                        p4 VARCHAR(45) NOT NULL,
                        p5 VARCHAR(45) NOT NULL,
                        p6 VARCHAR(45) NOT NULL,
                        p7 VARCHAR(45) NOT NULL,
                        p8 VARCHAR(45) NOT NULL);
                        )'''
                    cursor.execute(sql)
                    con.close()
                    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
                    cursor = con.cursor()

                mySql_insert_query = "INSERT INTO time4his VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
                cursor.execute(mySql_insert_query)
                con.commit()
            format_row = "{:>9}" * (len(table) + 1)
          #  print(format_row.format("", *table))
            for team, row in zip(table, data_items):
                pass
               # print(format_row.format(team, *row))
    cursor.execute("DROP TABLE IF EXISTS time5")
    sql ='''CREATE TABLE timetable.time5 (
    name VARCHAR(45) NOT NULL,
    day VARCHAR(45) NOT NULL,
    p1 VARCHAR(45) NOT NULL,
    p2 VARCHAR(45) NOT NULL,
    p3 VARCHAR(45) NOT NULL,
    p4 VARCHAR(45) NOT NULL,
    p5 VARCHAR(45) NOT NULL,
    p6 VARCHAR(45) NOT NULL,
    p7 VARCHAR(45) NOT NULL,
    p8 VARCHAR(45) NOT NULL);
    )'''
    cursor.execute(sql)
    con.close()
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()
    for sec1 in templist:
        week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
    #print("          1        2         3       4        5           6          7          8")
        data_items = []
        #print(c, len(fact), len(templist))
        fact1 = fact[templist.index(sec1)]
        #print(fact1)
        for p in fact1.keys():
            for w in range(6):
                x = []
                x.append(p)
                x.append(week[w])
                for j in range(8):
                    for k in sec1[w]:
                        k = k[1:]
                        try:
                            if j + 1 in k[1]:
                                if len(k[1]) == 3:
                                    x.append(k[2] + "lab")
                            #print(k[2], end = "lab     ")
                                    break
                        except:
                            if j + 1 == k[1]:
                                x.append(k[2])
                                break
                            else:
                                continue
                    else:
                        x.append("----")
                data_items.append(x)
               # print(x)
                mySql_insert_query = "INSERT INTO time5 VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
                cursor = con.cursor()
                cursor.execute(mySql_insert_query)
                con.commit()
                #print(x)
    table = ['Day', '1', '2', '3', '4', '5', '6', '7', '8']
    cursor.execute("DROP TABLE IF EXISTS time6")
    sql ='''CREATE TABLE timetable.time6 (
    name VARCHAR(45) NOT NULL,
    day VARCHAR(45) NOT NULL,
    p1 VARCHAR(45) NOT NULL,
    p2 VARCHAR(45) NOT NULL,
    p3 VARCHAR(45) NOT NULL,
    p4 VARCHAR(45) NOT NULL,
    p5 VARCHAR(45) NOT NULL,
    p6 VARCHAR(45) NOT NULL,
    p7 VARCHAR(45) NOT NULL,
    p8 VARCHAR(45) NOT NULL);
    )'''
    cursor.execute(sql)
    con.close()
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()
    for i in faculty:
        if i[4].count(0) == 6:
            continue
        print("         " + i[0] + "           ")
        data_items = []
        c = 0
        for w in range(6):
            x = []
            x.append(i[0])
            x.append(week[w])
            for j in range(8):
                try:
                    if j + 1 in i[4][w]:
                        if len(i[4]) == 6:
                            x.append(i[5][-2])
                        else:
                            x.append(i[4][-1])
                            continue
                except:
                    if j + 1 == i[4][w]:
                        x.append(i[4][-1])
                        continue
                try:
                    if j + 1 in i[5][w]:
                        x.append(i[5][-1])
                        continue
                except:
                    if j + 1 == i[5][w]:
                        x.append(i[5][-1])
                        continue
                try:
                    if j + 1 in i[6][w]:
                        x.append(i[6][-1])
                        continue
                except:
                    if j + 1 == i[6][w]:
                        x.append(i[6][-1])
                        continue
                x.append("----")
            data_items.append(x)
          #  print(x)
            mySql_insert_query = "INSERT INTO time6 VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
            #cursor = con.cursor()
            cursor.execute(mySql_insert_query)
            con.commit()
          #  print(x)
   
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
                <div class="card" id="generatePDF">

            <center> <h2> Time Table Created </h2>
            <br><br>
            </center>
                
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
    </div>
    </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
        </script>
            </body>
            </html>
            '''

    filename = 'demo21.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')

@app.route('/factEvenSubjects')
def factEvenSubjects():
   # print("HI")
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from timedicteven"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    yearSec = ["ICSEA","ICSEB","ICSEC","IICSEA" ,"IICSEB","IICSEC","IIICSEA","IIICSEB","IIICSEC"]
    answer1 = []
    answer = []
    c = 0
    tbl = "<tr><td>Username</td><td>Section</td><td>Subject</td></tr>"
    answer.append(tbl)
    for i in records:
      #  print(i)
        a1 = "<td>%s</td>" % i[0]
        answer.append(a1)
        a2 = "<td>%s</td>" % i[1]
        answer.append(a2)
        a9 = "<td>%s</td></tr>" % i[2]
        answer.append(a9)    
        answer1.append(answer)

    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
 <div class="card" id="generatePDF">
            <center> <h2> Faculty Allocation </h2>
            <table border = 1>
            %s
            </table>
            </center>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''%(answer1[0])

    filename = 'demo24.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


@app.route('/x')
def x():
   # print("HI")
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time4"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    yearSec = ["ICSEA","ICSEB","ICSEC","IICSEA" ,"IICSEB","IICSEC","IIICSEA","IIICSEB","IIICSEC"]
    answer1 = ['.'] * 50
    c = 0
    tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr>"
    #print(len(records))
    for i in range(0, len(records), 6):
        record = records[i : i + 6]
        answer = []
        answer.append(tbl)
        for j in record:
                #print(record)
                a1 = "<td>%s</td>" % j[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % j[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % j[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % j[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % j[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % j[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % j[7]
                answer.append(a7)
                a8 = "<td>%s</td>" % j[8]
                answer.append(a8)
                a9 = "<td>%s</td></tr>" % j[9]
                answer.append(a9)
                
        answer1[c] = answer 
        c += 1
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
 <div class="card" id="generatePDF">
            <center>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            </center>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''%(yearSec[0], answer1[0], yearSec[1], answer1[1],yearSec[2], answer1[2],yearSec[3], answer1[3], yearSec[4], answer1[4], yearSec[5], answer1[5],yearSec[6], answer1[6], yearSec[7], answer1[7], yearSec[8], answer1[8])

    filename = 'demo29.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    
    return render_template('demo2.html') 



@app.route('/factdasheven')
def factdasheven():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from timedicteven"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    answer = [['.', '.'], ['.', '.'],['.', '.'],['.', '.']]
    goal = c1.name
    c = 0
    for i in records:
        if i[0][:len(i[0]) - 4].lower() == goal:
            answer[c][0] = i[1]
            answer[c][1]  =  i[2]
            c += 1
           # print(i[1], i[2])
           # print(answer)
   # print(answer)
    return render_template('factdasheven.html', n1 = c1.Name, d1 = c1.dept, e = c1.email, d = c1.deg, p1 = c1.pre1, p2 = c1.pre2, p3 = c1.pre3, p4 = c1.pre4, p5 = c1.name, y1 = answer[0][0], s1 = answer[0][1], y2 = answer[1][0], s2 = answer[1][1],  y3 = answer[2][0], s3 = answer[2][1])

@app.route('/factdashodd')
def factdashodd():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from timedict"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    answer = [['.', '.'], ['.', '.'],['.', '.'],['.', '.']]
    goal = c1.name
    c = 0
    for i in records:
        if i[0][:len(i[0]) - 4].lower() == goal:
            answer[c][0] = i[1]
            answer[c][1]  =  i[2]
            c += 1
          #  print(i[1], i[2])
           # print(answer)
    #print(answer)
    return render_template('factdashodd.html', n1 = c1.Name, d1 = c1.dept, e = c1.email, d = c1.deg, p1 = c1.pre1, p2 = c1.pre2, p3 = c1.pre3, p4 = c1.pre4, p5 = c1.name, y1 = answer[0][0], s1 = answer[0][1], y2 = answer[1][0], s2 = answer[1][1],  y3 = answer[2][0], s3 = answer[2][1])


@app.route('/classeven')
def classeven():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time5"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    table = ['Day', '1', '2', '3', '4', '5', '6', '7', '8']
    week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
    c2 = 0
    goal = c1.name
    f = 0
    ans = []
    answer1 = ['.'] * 4
    answer2 = ['.'] * 4
    counter = 0
    #con1 = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query1 = "select * from timedict"
    cursor1 = con.cursor()
    cursor1.execute(query1)
    records1 = cursor.fetchall()
  #  print(records1)
    for i in records1:
       # print(i[0])
        if i[0][:len(i[0]) - 4].lower() == goal:
            answer2[counter] = i[1]
            counter += 1  

    sections = ["ICSEA", "ICSEB", "ICSEC", "IICSEA", "IICSEB", "IICSEC", "IIICSEA", "IIICSEB","IIICSEC", '.', '.', '.', '.', '.', '.', '.', '.']
    idx = [0] * 4
    count = 0
    idxcount = -1
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        idxcount += 1
        data_items = []
        answer = []
        if records[c2][0][:len(records[c2][0]) - 4].lower() == goal:
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            idx[count] = idxcount
            count += 1
        else:
            c2 += 1
    #print(idx)
    if f == 0:
        print("No period assigned")
    c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
 <div class="card" id="generatePDF">
            <br><br>
         
            <center>
            <h3>%s</h3>
            <table border = 1>
            %s
            </table>
            </center>
            <br><br>
            
            <center>
            <h3>%s</h3>
            <table border = 1>
            %s
            </table>
            </center>
            <br><br>
           
           <center>
           <h3>%s</h3>
            <table border = 1>
            %s
            </table>
            </center>
            <br><br>
            
            <center>
            <h3>%s</h3>
            <table border = 1>
            %s
            </table>
            </center>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''%(answer2[0], answer1[0],answer2[1],answer1[1],answer2[2],answer1[2],answer2[3], answer1[3])

    filename = 'demo11.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    
    return render_template('demo1.html', n1 = c1.name, n2 = ans) 

@app.route('/indieven')
def indieven():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time6"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    table = ['Day', '1', '2', '3', '4', '5', '6', '7', '8']
    week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
    c2 = 0
    goal = c1.name
    f = 0
    ans = []
    answer1 = ['.'] * 4
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0][:len(records[c2][0]) - 4].lower() == goal:
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <div class="card" id="generatePDF">

            <br><br>
            <center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <table border = 1>
            %s
            </table>
            <br><br>
            <table border = 1>
            %s
            </table>
            <br><br>
            <table border = 1>
            %s
            </table>
              <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>

            </body>
            </html>
            '''%(answer1[0], answer1[1], answer1[2], answer1[3])

    filename = 'demo12.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    
    return render_template('demo2.html', n1 = c1.name, n2 = ans) 
    


















@app.route('/factSubjects')
def factSubjects():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from timedict"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    yearSec = ["ICSEA","ICSEB","ICSEC","IICSEA" ,"IICSEB","IICSEC","IIICSEA","IIICSEB","IIICSEC"]
    answer1 = []
    answer = []
    c = 0
    tbl = "<tr><td>Username</td><td>Section</td><td>Subject</td></tr>"
    answer.append(tbl)
    for i in records:
        a1 = "<td>%s</td>" % i[0]
        answer.append(a1)
        a2 = "<td>%s</td>" % i[1]
        answer.append(a2)
        a9 = "<td>%s</td></tr>" % i[2]
        answer.append(a9)    
        answer1.append(answer)

    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
 <div class="card" id="generatePDF">
            <center> <h2> Faculty Allocation </h2>
            <table border = 1>
            %s
            </table>
            </center>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''%(answer1[0])

    filename = 'demo4.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')

        


@app.route('/generateTimeTable')
def generateTimeTable():
    def generateTimeTable():
        try:
            templist = []
            fact = []
            sem1 = ["ENG1", "AP", "C", "BEE1", "M1", ["ENG1", "AP", "C"]]
            sem2 = ["BEE2", "EC", "DS", "PYTHON", "M2", ["EC", "PYTHON", "DS"]]
            sem3 = ["JAVA", "DM", "PS", "SE", "DLD", ["JAVA", "DV", "CMHW", "ARTS"]]
            sem4 = ["ENG2", "WT", "OR", "DBMS", "COA", ["WT", "DBMS", "OOAD", 'JP']]
            sem5 = ["OS", "DAA", "DMDW", "SS", "TOC", ["GD", 'IOT', 'LP', 'CD']]
            sem6 = ["CN" , "FSD" , "MP" , "DAS" , "CS"]
            totalSem = [["ENG", "AP", "C", "BEE1", "M1"], ["BEE2", "EC", "DS", "PYTHON", "M2"], ["JAVA", "DM", "PS", "SE", "DLD"], ["ENG2", "WT", "OR", "DBMS", "COA"], ["OS", "DAA", "DMDW", "SS", "TOC"], ["CN" , "FSD" , "MP" , "DAS" , "CS"]]
            faculty = [["sudha mam", 8, ["WT", "JAVA", "CN", "PYTHON"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["ramarao sir", 7, ["WT", "DLD", "DM", 'LP'], 4, [0] * 6, [0] * 6, [0] * 6],
            ["kesava sir", 8, ["WT", 'LP', "CMHW"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["darmaiah sir", 8, ["WT", 'LP', "CMHW"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["ravikiran sir", 10, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["vasubabu sir", 10, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["kameswari mam", 10, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["murthy sir", 9, ["OR", "M1", "M2", "PS"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["G.ramesh babu sir", 1, ["COA", "DAA", "DLD", "GD"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["srikanth sir", 2, ["COA", "DAA", "DM",  "DV"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["prasad sir", 2, ["COA", "DAA", "DM",  "DV"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["purushothamaraju sir", 15, ["DBMS", "DMDW", "OS", "CN"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["ramachandraroa sir", 12,  ["DBMS", "DMDW", "OS", "CN"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["srihariraju sir", 12,  ["ENG1", "SS", "SS2", "ENG2"], 4, [0] * 6, [0] * 6, [0] * 6], 
            ["devi mam", 7,  ["ENG1", "SS", "SS2", "ENG2"],4,[0] * 6, [0] * 6,[0] * 6],
            ["M.ramesh babu sir",7,["DM","MP","CS", "OOAD", "IOT"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["P.Raju sir",7,["DM","MP","CS", "OOAD", "IOT"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Dharmaih sir",7,["DM","MP","CS", "OOAD", "IOT"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Kalpana mam",7,["SE","OS", "CS"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Durga mam",0,["SE","OS","CD","CS"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Archana mam",7,["SE","OS","CD","CS", "CD"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Soni mam",7,["SE","OS","CD","CS", "CD", "GD"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["V.V.R.Maheshwara Rao sir",10,["SE","OS","CD","DM"], 4 ,[0] * 6, [0] * 6,[0] * 6],
            ["Shalem Raju sir",9,["TOC","MP","DM","CD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Tharaka satyanaran sir",2,["TOC","MP","DM","CD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Sunil sir",8 ,["DS","PYTHON","DAA","TOC"], 4 ,[0] * 6, [0] * 6, [0] * 6, []],
            ["Gayathri mam",7,["COA","PYTHON","C","CD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Silpa mam",9,["C","SE","OS","CS"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Swathi mam",8,["C","PYTHON","DS","FSD"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Seenu sir", 9, ["C", "PYTHON", "JAVA", "MC"], 4, [0] * 6, [0] * 6, [0] * 6],
            ["Phaneendhra varma sir",2,["FSD","CS","JAVA","DAS", 'GD'], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Srinivas sir",9,["AP","EP","P1","P2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Bhramhanandam sir",8,["AP","EP","P1","P2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Jagadeesh sir",10,["EC","AC","C1","C2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Ganesh sir",10,["EC","AC","C1","C2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Arun sir",7,["ENG1","ENG2","SS","SS2"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Swaroop sir",6,["BEE1","BEE2","AP","EP"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Narayana kiran sir",5,["BEE1","BEE2","AP","EP"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Kalyan sagar sir",4,["BEE1","BEE2","AP","EP"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []],
            ["Ramu sir",9,["DMDW","DBMS","DAS","CS"], 4 ,[0] * 6, [0] * 6,[0] * 6 , []],
            ["Ratna kumari mam",9,["DMDW","DBMS","DAS","CS", "JP", "ARTS"], 4 ,[0] * 6, [0] * 6, [0] * 6 , []]]
            faculty = sorted(faculty, key = lambda x : x[1], reverse = True)
            week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
            count = 0
            def mainFunction(subjects, labs, sem):
            
                factDict = {}
        #labs = [0, 1, 2]
                sec1 = []
                weeks = [0,1,2,3,4,5]
                w = 0
                while weeks:
                    w += 1
                    sec2 = []
                    ranWeek = random.choice(weeks)
                    subjectIndex = [0,1,2,3,4]
                    days = [1, 2, 3, 4, 5, 6, 7, 8]
                    labDays = [2, 6]
                    if labs:
                        ranLab = random.choice(labs)
                        lab = subjects[5][ranLab]
                        labs.remove(ranLab)
                        for i in faculty:
                            if lab in i[2]:
                                if i[4].count(0) != 0 and i[3] > 3:
                                
                                    if lab in factDict.values():
            
                                        try:
                                            if factDict[i[0]] == lab:
                                                randomDay = random.choice(labDays)
                                                labDays.remove(randomDay)
                                                days.remove(randomDay)
                                                days.remove(randomDay + 1)
                                                days.remove(randomDay + 2)
                                                i[4][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                            
                                                i[3] -= 1
                                                sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                                break
                                        except:
                                            continue
                                    else:
                                        factDict[i[0]] = lab
                                        randomDay = random.choice(labDays)
                                        labDays.remove(randomDay)
                                        days.remove(randomDay)
                                        days.remove(randomDay + 1)
                                        days.remove(randomDay + 2)
                                    
                                        i[4][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                    
                                        i[3] -= 1
                                        sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                        break
                           

                                elif i[5].count(0) != 0 and i[3] >= 3:
                                    if lab in factDict.values():
                                        try:
                                            if factDict[i[0]] == lab:
                                                f = 0
                                                try:
                                                    if i[4][ranWeek][0] in labDays:
                                                        x.append(i[4][ranWeek][0])
                                                        labDays.remove(i[4][ranWeek][0])
                                                        f = 1
                                                    if i[4][ranWeek][4] in labDays:
                                                        x.append(i[4][ranWeek][4])
                                                        labDays.remove(i[4][ranWeek][4])
                            
                                                except:
                                                    if i[4][ranWeek] in [2,3,4] and 2 in labDays:
                                                        x = 2
                                                        labDays.remove(2)
                                                        f = 1 
                                                    elif i[4][ranWeek] in [8,6,7] and 6 in labDays:
                                                        x = 6
                                                        labDays.remove(6)
                                                        f = 1
                                                randomDay = random.choice(labDays)
                                            labDays.remove(randomDay)
                                            days.remove(randomDay)
                                            days.remove(randomDay + 1)
                                            days.remove(randomDay + 2)
                                       
                                            i[3] -= 1
                                            i[5][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                            sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                            if f == 1:
                                                try:
                                                    labDays.extend(x)
                                                except:
                                                    labDays.append(x)
                                            break
                                        except:
                                            continue
                                    else:
                                            factDict[i[0]] = lab
                                            f = 0
                                            try:
                                                if i[4][ranWeek][0] in labDays:
                                                    x.append(i[4][ranWeek][0])
                                                    labDays.remove(i[4][ranWeek][0])
                                                    f = 1
                                                if i[4][ranWeek][4] in labDays:
                                                    x.append(i[4][ranWeek][4])
                                                    labDays.remove(i[4][ranWeek][4])
                            
                                            except:
                                                if i[4][ranWeek] in [2,3,4] and 2 in labDays:
                                                    x = 2
                                                    labDays.remove(2)
                                                    f = 1 
                                                elif i[4][ranWeek] in [8,6,7] and 6 in labDays:
                                                    x = 6
                                                    labDays.remove(6)
                                                    f = 1
                                            randomDay = random.choice(labDays)
                                            labDays.remove(randomDay)
                                            days.remove(randomDay)
                                            days.remove(randomDay + 1)
                                            days.remove(randomDay + 2)
                                            
                                            i[3] -= 1
                                            i[5][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                            sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                            if f == 1:
                                                try:
                                                    labDays.extend(x)
                                                except:
                                                    labDays.append(x)
                            
                                            break
                                elif lab not in subjects[:6] and i[3] >= 2 and i[4].count(0) != 0 and i[5].count(0) != 0:
                                
                                    factDict[i[0]] = lab
                                    if i[4][ranWeek] == 0:
                                        pass
                                    elif i[4][ranWeek][0] in labDays:
                                        x = i[4][ranWeek][0]
                                        labDays.remove(i[4][ranWeek][0])
                                    if i[5][ranWeek] == 0:
                                        pass 
                                    elif i[5][ranWeek][0] in labDays:
                                        y = i[5][ranWeek][0]
                                        labDays.remove(i[5][ranWeek][0])
                                    randomDay = random.choice(labDays)
                                    labDays.remove(randomDay)
                                    days.remove(randomDay)
                                    days.remove(randomDay + 1)
                                    days.remove(randomDay + 2)
                                    i[3] -= 1
                                    i[6][ranWeek] = [randomDay, randomDay + 1, randomDay + 2]
                                    sec2.append([ranWeek, i[0], [randomDay, randomDay + 1, randomDay + 2], lab])
                                    try:
                                        labDays.append(x)
                                    except:
                                        continue
                                    try:
                                        labDays.append(y)
                                    except:
                                        continue
                                else:
                                    continue       
                                
                    day = 0
       #print(days, randomDay)
                    while subjectIndex:
                   # print(days)
                        day += 1
                   # randomPeriod = random.choice(days)
                        ran = random.choice(subjectIndex)
                        subject = subjects[ran]
                        subjectIndex.remove(ran)
                        for i in faculty:
                            if subject in i[2] and i[3] >= 2:
                                if subject in factDict.values():
                                    try:
                                        if factDict[i[0]] == subject:
                                            if i[4].count(0) != 0:
                                            
                                                randomPeriod = random.choice(days)
                                        #print("Hello")
                                                if i[4][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                    i[4][ranWeek].append(randomPeriod)
                                                else:
                                           # i[4].append([randomPeriod, classes])
                                                    i[4][ranWeek] = randomPeriod
                                                sec2.append([ranWeek, i[0], randomPeriod, subject])
                                                if w == 1 and subject not in subjects[5]:
                                                    i[3] -= 1
                                                break
                                            else:
                                           # print(i[4], i[0])
                                                a = 0
                                                y = []
                                                try:
                                                    x = len(i[4][ranWeek])
                                                    a = 1 
                                                except:
                                                    x = 0
                                                    pass 
                                                if a == 1:
                                                    if (i[4][ranWeek][0] in days):
                                                        days.remove(i[4][ranWeek][0])
                                                        y.append(i[4][ranWeek][0])
                                                    if (i[4][ranWeek][1] in days):
                                                        days.remove(i[4][ranWeek][1])
                                                        y.append(i[4][ranWeek][1])
                                                    if (i[4][ranWeek][2] in days):
                                                        days.remove(i[4][ranWeek][2])
                                                        y.append(i[4][ranWeek][2])
                                                    if len(i[4][ranWeek]) >= 4 and i[4][ranWeek][3] in days:
                                                        days.remove(i[4][ranWeek][3])
                                                        y.append(i[4][ranWeek][3])
                                                else:
                                                    if i[4][ranWeek] in days:
                                                        days.remove(i[4][ranWeek])
                                                        y.append(i[4][ranWeek])
                                                randomPeriod = random.choice(days)
                                                if w == 1 and subject not in subjects[5]:
                                                    i[3] -= 1

                                                if i[5][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                    i[5][ranWeek].append(randomPeriod)
                                                else:
                                           # i[4].append([randomPeriod, classes])
                                                    i[5][ranWeek] = randomPeriod
                                        
                                                sec2.append([ranWeek, i[0], randomPeriod, subject])
                                                try:
                                                    days.extend(y)
                                                except:
                                                    days.append(y)
                                                break 

                                        
                                    except:
                                        continue
                                elif i[5].count(0) != 0:
                                    if i[0] not in factDict:
                                        factDict[i[0]] = subject
                                        if i[4].count(0) != 0:
                                    #print("Hello")
                                                randomPeriod = random.choice(days)
                                           # i[4].append([randomPeriod, classes])
                                                if i[4][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                    i[4][ranWeek].append(randomPeriod)
                                                else:
                                           # i[4].append([randomPeriod, classes])
                                                    i[4][ranWeek] = randomPeriod
                                                if w == 1 and subject not in subjects[5]:
                                                    i[3] -= 1
                                                sec2.append([ranWeek, i[0], randomPeriod, subject])
                                                break
                                        else:
                                       
                                            a = 0
                                            y = []
                                            try:
                                                x = len(i[4][ranWeek])
                                                a = 1 
                                            except:
                                                x = 0
                                                pass 
                                            if a == 1:
                                                if (i[4][ranWeek][0] in days):
                                                    days.remove(i[4][ranWeek][0])
                                                    y.append(i[4][ranWeek][0])
                                                if (i[4][ranWeek][1] in days):
                                                    days.remove(i[4][ranWeek][1])
                                                    y.append(i[4][ranWeek][1])
                                                if (i[4][ranWeek][2] in days):
                                                    days.remove(i[4][ranWeek][2])
                                                    y.append(i[4][ranWeek][2])
                                                if len(i[4][ranWeek]) >= 4 and (i[4][ranWeek][3] in days):
                                                    days.remove(i[4][ranWeek][3])
                                                    y.append(i[4][ranWeek][3])
                                            else:
                                                if i[4][ranWeek] in days:
                                                    days.remove(i[4][ranWeek])
                                                    y.append(i[4][ranWeek])
                                            randomPeriod = random.choice(days)
                                            
                                            if i[5][ranWeek] not in [0,1,2,3,4,5,6,7,8]:
                                                i[5][ranWeek].append(randomPeriod)
                                            else:
                                           # i[4].append([randomPeriod, classes])
                                                i[5][ranWeek] = randomPeriod
                                            if w == 1 and subject not in subjects[5]:
                                                i[3] -= 1
                                            sec2.append([ranWeek, i[0], randomPeriod, subject])
                                            try:
                                                days.extend(y)
                                            except:
                                                days.append(y)
                                            days = list(set(days))
                                            break 

                                    else:
                                        continue
                                else:
                                    continue
                            else:
                                continue
                   # print(days, randomPeriod)
                        days.remove(randomPeriod)
                    
                    sec1.append((sec2))
        #print(sec2)
                    weeks.remove(ranWeek)
                sec1 = sorted(sec1, key = lambda x : x[0][0])
                for k, v in factDict.items():
                    for i in faculty:
                        if k == i[0]:
                            if i[6].count(0) != 6:
                                i[6].append(sem)
                            elif i[5].count(0) != 6:
                                i[5].append(sem)
                            elif i[4].count(0) != 6:
                                i[4].append(sem)
                        else:
                            continue
            #print(factDict)
           
                return sec1, factDict
            x = mainFunction(sem1, [0, 1, 2], "ICSEA")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem1, [0, 1, 2], "ICSEB")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem1, [0, 1, 2], "ICSEC")
            templist.append(x[0])
            fact.append(x[1])
        #templist.append(mainFunction(sem2, [0, 1, 2]))
            x = mainFunction(sem3, [0, 1, 2, 3], "IICSEA")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem3, [0, 1, 2, 3], "IICSEB")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem3, [0, 1, 2, 3], "IICSEC")
            templist.append(x[0])
            fact.append(x[1])
            #templist.append(mainFunction(sem4, [0, 1, 2, 3]))
            x = mainFunction(sem5, [0, 1, 2, 3], "IIICSEA")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem5, [0, 1, 2, 3], "IIICSEB")
            templist.append(x[0])
            fact.append(x[1])
            x = mainFunction(sem5, [0, 1, 2, 3], "IIICSEC")
            templist.append(x[0])
            fact.append(x[1])
            return templist, fact, faculty, False
        except Exception as e:
        #print(e)
            return templist, fact, faculty, True
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    
    flag = True 
    goal = "sudha mam"
    while flag:
        templist,fact, faculty, flag = generateTimeTable()
    for i in fact:
       # print(i)
        print("...................................")
    table = ['sec', 'Day', '1', '2', '3', '4', '5', '6', '7', '8']
    #print(templist)
    yearSec = ["ICSEA","ICSEB","ICSEC","IICSEA" ,"IICSEB","IICSEC","IIICSEA","IIICSEB","IIICSEC"]
    c = -1
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS time3")
    sql ='''CREATE TABLE timetable.time3 (
    sec VARCHAR(45) NOT NULL,
    day VARCHAR(45) NOT NULL,
    p1 VARCHAR(45) NOT NULL,
    p2 VARCHAR(45) NOT NULL,
    p3 VARCHAR(45) NOT NULL,
    p4 VARCHAR(45) NOT NULL,
    p5 VARCHAR(45) NOT NULL,
    p6 VARCHAR(45) NOT NULL,
    p7 VARCHAR(45) NOT NULL,
    p8 VARCHAR(45) NOT NULL);
    )'''
    cursor.execute(sql)
    con.close()
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()
    for sec1 in templist:
            c += 1
            week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
        #print("          1        2         3       4        5           6          7          8")
            data_items = []
            #print(c, len(fact), len(templist))
            fact1 = fact[templist.index(sec1)]
            print("..............................." + yearSec[c] + "............................")
            #print(fact1)
            for w in range(6):
                    x = []
                    x.append(yearSec[c])
                    #x.append(p)
                    x.append(week[w])
                    for j in range(8):
                        for k in sec1[w]:
                            k = k[1:]
                            try:
                                if j + 1 in k[1]:
                                    if len(k[1]) == 3:
                                        x.append(k[2] + "lab")
                                #print(k[2], end = "lab     ")
                                        break
                            except:
                                if j + 1 == k[1]:
                                    x.append(k[2])
                                    break
                                else:
                                    continue
                        else:
                            x.append("----")
                    data_items.append(x)
                    mySql_insert_query = "INSERT INTO time3 VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
                    cursor.execute(mySql_insert_query)
                    con.commit()
                    query = "select * from time3his"
                    cursor = con.cursor()
                    cursor.execute(query)
                    records = cursor.fetchall()
                    if len(records) == 54 * 3:
                        cursor = con.cursor()
                        cursor.execute("DROP TABLE IF EXISTS time3his")
                        sql ='''CREATE TABLE timetable.time3his (
                        sec VARCHAR(45) NOT NULL,
                        day VARCHAR(45) NOT NULL,
                        p1 VARCHAR(45) NOT NULL,
                        p2 VARCHAR(45) NOT NULL,
                        p3 VARCHAR(45) NOT NULL,
                        p4 VARCHAR(45) NOT NULL,
                        p5 VARCHAR(45) NOT NULL,
                        p6 VARCHAR(45) NOT NULL,
                        p7 VARCHAR(45) NOT NULL,
                        p8 VARCHAR(45) NOT NULL);
                        )'''
                        cursor.execute(sql)
                        con.close()
                        con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
                        cursor = con.cursor()
                    mySql_insert_query = "INSERT INTO time3his VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
                    cursor.execute(mySql_insert_query)
                    con.commit()
            format_row = "{:>9}" * (len(table) + 1)
            #print(format_row.format("", *table))
            for team, row in zip(table, data_items):
                pass
               # print(format_row.format(team, *row))
    cursor.execute("DROP TABLE IF EXISTS time1")
    sql ='''CREATE TABLE timetable.time1 (
    name VARCHAR(45) NOT NULL,
    day VARCHAR(45) NOT NULL,
    p1 VARCHAR(45) NOT NULL,
    p2 VARCHAR(45) NOT NULL,
    p3 VARCHAR(45) NOT NULL,
    p4 VARCHAR(45) NOT NULL,
    p5 VARCHAR(45) NOT NULL,
    p6 VARCHAR(45) NOT NULL,
    p7 VARCHAR(45) NOT NULL,
    p8 VARCHAR(45) NOT NULL);
    )'''
    cursor.execute(sql)
    con.close()
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()
    for sec1 in templist:
        week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
    #print("          1        2         3       4        5           6          7          8")
        data_items = []
        #print(c, len(fact), len(templist))
        fact1 = fact[templist.index(sec1)]
        #print(fact1)
        for p in fact1.keys():
            for w in range(6):
                x = []
                x.append(p)
                x.append(week[w])
                for j in range(8):
                    for k in sec1[w]:
                        k = k[1:]
                        try:
                            if j + 1 in k[1]:
                                if len(k[1]) == 3:
                                    x.append(k[2] + "lab")
                            #print(k[2], end = "lab     ")
                                    break
                        except:
                            if j + 1 == k[1]:
                                x.append(k[2])
                                break
                            else:
                                continue
                    else:
                        x.append("----")
                data_items.append(x)
               # print(x)
                mySql_insert_query = "INSERT INTO time1 VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
                cursor = con.cursor()
                cursor.execute(mySql_insert_query)
                con.commit()
                #print(x)
    table = ['Day', '1', '2', '3', '4', '5', '6', '7', '8']
    yearSec = ["ICSEA","ICSEB","ICSEC","IICSEA" ,"IICSEB","IICSEC","IIICSEA","IIICSEB","IIICSEC"]
    c = -1
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()
    cursor.execute("DROP TABLE IF EXISTS timedict")
    sql = '''CREATE TABLE timetable.timedict (
    uname VARCHAR(45) NOT NULL,
    year VARCHAR(45) NOT NULL,
    subject VARCHAR(45) NOT NULL);
    )'''
    cursor.execute(sql)
    con.close()
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()

    for i in fact:
        c += 1
        for k, v in i.items():
            mySql_insert_query = "INSERT INTO timedict VALUES('"+k+"', '"+yearSec[c]+"', '"+v+"');"
            cursor.execute(mySql_insert_query)
            con.commit()

    cursor.execute("DROP TABLE IF EXISTS time2")
    sql ='''CREATE TABLE timetable.time2 (
    name VARCHAR(45) NOT NULL,
    day VARCHAR(45) NOT NULL,
    p1 VARCHAR(45) NOT NULL,
    p2 VARCHAR(45) NOT NULL,
    p3 VARCHAR(45) NOT NULL,
    p4 VARCHAR(45) NOT NULL,
    p5 VARCHAR(45) NOT NULL,
    p6 VARCHAR(45) NOT NULL,
    p7 VARCHAR(45) NOT NULL,
    p8 VARCHAR(45) NOT NULL);
    )'''
    cursor.execute(sql)
    con.close()
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    cursor = con.cursor()
    for i in faculty:
        if i[4].count(0) == 6:
            continue
        #print("         " + i[0] + "           ")
        data_items = []
        c = 0
        for w in range(6):
            x = []
            x.append(i[0])
            x.append(week[w])
            for j in range(8):
                try:
                    if j + 1 in i[4][w]:
                        if len(i[4]) == 6:
                            x.append(i[5][-2])
                        else:
                            x.append(i[4][-1])
                        continue
                except:
                    if j + 1 == i[4][w]:
                        x.append(i[4][-1])
                        continue
                try:
                    if j + 1 in i[5][w]:
                        x.append(i[5][-1])
                        continue
                except:
                    if j + 1 == i[5][w]:
                        x.append(i[5][-1])
                        continue
                try:
                    if j + 1 in i[6][w]:
                        x.append(i[6][-1])
                        continue
                except:
                    if j + 1 == i[6][w]:
                        x.append(i[6][-1])
                        continue
                x.append("----")
            data_items.append(x)
            #print(x)
            mySql_insert_query = "INSERT INTO time2 VALUES('"+x[0]+"', '"+x[1]+"', '"+x[2]+"', '"+x[3]+"','"+x[4]+"', '"+x[5]+"','"+x[6]+"','"+x[7]+"','"+x[8]+"', '"+x[9]+"');"
                #cursor = con.cursor()
            cursor.execute(mySql_insert_query)
            con.commit()
           # print(x)
        format_row = "{:>9}" * (len(table) + 1)
       # print(format_row.format("", *table))
        for team, row in zip(table, data_items):
            pass
           # print(format_row.format(team, *row))
        print("...........................................................")
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
 <div class="card" id="generatePDF">
            <center> <h2> Time Table Created </h2>
            <br><br>
            </center>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''

    filename = 'demo5.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


@app.route('/ViewTimeTable')
def ViewTimeTable():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time1"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    yearSec = ["ICSEA","ICSEB","ICSEC","IICSEA" ,"IICSEB","IICSEC","IIICSEA","IIICSEB","IIICSEC"]
    answer1 = ['.'] * 100
    c = 0
    tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr>"
    #print(len(records))
    for i in range(0, len(records), 6):
        record = records[i : i + 6]
        answer = []
        answer.append(tbl)
        for j in record:
                #print(record)
                a1 = "<td>%s</td>" % j[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % j[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % j[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % j[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % j[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % j[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % j[7]
                answer.append(a7)
                a8 = "<td>%s</td>" % j[8]
                answer.append(a8)
                a9 = "<td>%s</td></tr>" % j[9]
                answer.append(a9)
                
        answer1[c] = answer 
        c += 1
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
 <div class="card" id="generatePDF">
            <center>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            <br><br>
            <center><h3>%s</h3></center>
            <table border = 1>
            %s
            </table>
            </center>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''%(yearSec[0], answer1[0], yearSec[1], answer1[1],yearSec[2], answer1[2],yearSec[3], answer1[3], yearSec[4], answer1[4], yearSec[5], answer1[5],yearSec[6], answer1[6], yearSec[7], answer1[7], yearSec[8], answer1[8])

    filename = 'demo8.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    
    return render_template('demo2.html') 


@app.route('/admindasheven')
def admindasheven():
    return render_template('admindasheven.html', n1 = "Dr.Kiran Sree", d1 = "CSE", e = "kiransree@gmail.com", d = "HOD")



@app.route('/admindashodd')
def admindashodd():
    return render_template('admindashodd.html', n1 = "Dr.Kiran Sree", d1 = "CSE", e = "kiransree@gmail.com", d = "HOD")

@app.route('/factDetails')
def factDetails():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from faculty"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    answer = []
    tbl = "<tr><td>Username</td><td>Password</td><td>Name</td><td>Department</td><td>Email</td><td>Designation</td>"
    answer.append(tbl)
    for i in records:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
 <div class="card" id="generatePDF">
            <center> <h2> Faculty Details </h2>
            <br><br>
            <table border = 1>
            %s
            </table>
            </center>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''%(answer)

    filename = 'demo4.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')


@app.route('/factForm')
def factForm():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from facultyform"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    answer = []
    tbl = "<tr><td>Username</td><td>email</td><td>phone number</td><td>internal experience</td><td>pref 1</td><td>sem </td><td>pref 2</td><td>sem</td><td>pref 3</td><td>sem</td><td>pref 4</td><td>sem</td>"
    answer.append(tbl)
    for i in records:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td>" % i[8]
                answer.append(a8)
                a9 = "<td>%s</td>" % i[9]
                answer.append(a9)
                a10 = "<td>%s</td>" % i[10]
                answer.append(a10)
                a11 = "<td>%s</td></tr>" % i[11]
                answer.append(a11)
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
 <div class="card" id="generatePDF">
            <center> <h2> Faculty Preferences </h2></center>
            <br><br>
            <table border = 1>
            %s
            </table>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''%(answer)

    filename = 'demo3.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    return render_template('demo3.html')




@app.route('/getName', methods=['POST'])
def getName():
    sem1 = ["ENG1", "AP", "C", "BEE1", "M1", ["ENG1", "AP", "C"]]
    sem2 = ["BEE2", "EC", "DS", "PYTHON", "M2", ["EC", "PYTHON", "DS"]]
    sem3 = ["JAVA", "DM", "PS", "SE", "DLD", ["JAVA", "DV", "CMHW", "ARTS"]]
    sem4 = ["ENG2", "WT", "OR", "DBMS", "COA", ["WT", "DBMS", "OOAD", 'JP']]
    sem5 = ["OS", "DAA", "DMDW", "SS", "TOC", ["GD", 'IOT', 'LP', 'CD']]
    name1 = request.form['name']
    #print(c1.name)
    email1 = request.form['email']
    pn1 = request.form['pn']
    exp = request.form['experience']
    sub1 = request.form['sub1']
    sub2 = request.form['sub2']
    sub3 = request.form['sub3']
    sub4 = request.form['sub4']
    sems = []
    for i in [sub1, sub2, sub3, sub4]:
        if i in sem1:
            sems.append(1)
        if i in sem2:
            sems.append(2)
        if i in sem3:
            sems.append(3)
        if i in sem4:
            sems.append(4)
        if i in sem5:
            sems.append(5)
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    mySql_insert_query = "INSERT INTO facultyform VALUES ('{}', '{}', {}, {}, '{}', {}, '{}', {}, '{}', {}, '{}', {})".format(name1, email1, pn1, exp, sub1, sems[0], sub2, sems[1], sub3, sems[2], sub4, sems[3])
    cursor = con.cursor()
    cursor.execute(mySql_insert_query)
    con.commit()
    return render_template('submission.html', n1 = c1.name)
    
@app.route('/',methods=['POST'])
def getvalue():
    v = 'Have a nice day !'
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from faculty"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    query1 = "select * from time3his"
    cursor1 = con.cursor()
    cursor1.execute(query1)
    records1 = cursor.fetchall()
    if len(records1) == 54 * 3:
        v = "Danger! Time tables are going to be deleted. please save!"
    name1 = request.form['uname']
    c1.name = name1
    password1 = request.form['pwd1']
    p1 = "please fill preferences"
    p2 = "please fill preferences"
    p3 = "please fill preferences"
    p4 = "please fill preferences"
    for row in records:
        if row[0] == name1 and row[1] == password1:
            #print(row)
            name = row[2]
            dept = row[3]
            email = row[4]
            deg = row[5]
            query1 = "select * from facultyform"
            cursor1 = con.cursor()
            cursor1.execute(query1)
            records1 = cursor.fetchall()
            for row1 in records1:
                if row1[0] == name1:
                   # print(row1)
                    c1.Name = name
                    c1.dept = dept
                    c1.email = email 
                    c1.deg = deg 
                    c1.pre1 = row1[4] 
                    c1.pre2 = row1[6]
                    c1.pre3 = row1[8]
                    c1.pre4 = row1[10]
                    return render_template('factdash.html', n1 = name, d1 = dept, e = email, d = deg, p1 = row1[4], p2 = row1[6], p3 = row1[8], p4 = row1[10], p5 = c1.name, v1 = v)
            else:
                    c1.Name = name
                    c1.dept = dept
                    c1.email = email 
                    c1.deg = deg 
                    c1.pre1 = p1 
                    c1.pre2 = p2 
                    c1.pre3 = p3 
                    c1.pre4 = p4 
                    return render_template('factdash.html', n1 = name, d1 = dept, e = email, d = deg, p1 = "please fill preferences", p2 = "please fill preferences", p3 = "please fill preferences", p4 = "please fill preferences", v1 = v)

    else:
        return render_template('invalidfactlogin.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/Aboutus')
def Aboutus():
    return render_template('Aboutus.html')

@app.route('/preferences')
def preferences():
    c1.name = c1.name
    return render_template('preferences.html', n1 = c1.name) 

@app.route('/demo')
def demo():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time2"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    table = ['Day', '1', '2', '3', '4', '5', '6', '7', '8']
    week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
    c2 = 0
    goal = c1.name
    f = 0
    ans = []
    answer1 = ['.'] * 4
    count = 0
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        data_items = []
        answer = []
        if records[c2][0][:len(records[c2][0]) - 4].lower() == goal:
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            count += 1
        else:
            c2 += 1
            continue 
        if f == 0:
            print("No period assigned")
        c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
            <center>
 <div class="card" id="generatePDF">
            <br><br>
            <table border = 1>
            %s
            </table>
            <br><br>
            <table border = 1>
            %s
            </table>
            <br><br>
            <table border = 1>
            %s
            </table>
            <br><br>
            <table border = 1>
            %s
            </table>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''%(answer1[0], answer1[1], answer1[2], answer1[3])

    filename = 'demo2.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    
    return render_template('demo2.html', n1 = c1.name, n2 = ans) 
@app.route('/login1',methods=['POST'])
def login1():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    name1 = request.form['uname']
    pwd = request.form['pwd1']
    name2 = request.form['name']
    dept = request.form['dept']
    mail = request.form['mail']
    deg = request.form['deg']
    mySql_insert_query = "INSERT INTO faculty VALUES ('{}', '{}','{}', '{}','{}','{}')".format(name1, pwd, name2, dept, mail, deg)
    cursor = con.cursor()
    cursor.execute(mySql_insert_query)
    con.commit()
    return render_template('login.html') 

@app.route('/demo1')
def demo1():
    con = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query = "select * from time1"
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    table = ['Day', '1', '2', '3', '4', '5', '6', '7', '8']
    week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]
    c2 = 0
    goal = c1.name
    f = 0
    ans = []
    answer1 = ['.'] * 4
    answer2 = ['.'] * 4
    counter = 0
    #con1 = c1234.connect(host = "localhost", user = "root", passwd = "hari@9RUSHI", database = "timetable")
    query1 = "select * from timedict"
    cursor1 = con.cursor()
    cursor1.execute(query1)
    records1 = cursor.fetchall()
   # print(records1)
    for i in records1:
       # print(i[0])
        if i[0][:len(i[0]) - 4].lower() == goal:
            answer2[counter] = i[1]
            counter += 1  

    sections = ["ICSEA", "ICSEB", "ICSEC", "IICSEA", "IICSEB", "IICSEC", "IIICSEA", "IIICSEB","IIICSEC", '.', '.', '.', '.', '.', '.', '.', '.']
    idx = [0] * 4
    count = 0
    idxcount = -1
    #string1 = '<!DOCTYPE html> <html> <head> <meta content = "text/html; charset = UTF-8" http-equip = "content-type"><style>td {padding :0 15px;}</style><title>Time Table</title></head><body><br><br>'
    while c2 < (len(records)):
        idxcount += 1
        data_items = []
        answer = []
        if records[c2][0][:len(records[c2][0]) - 4].lower() == goal:
            f = 1
            for j in range(6):
                x = []
                x.extend(records[c2][1:])
                data_items.append(x)
                ans.append(data_items)
                c2 += 1
            tbl = "<tr><td>Day</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td>"
            answer.append(tbl)
            for i in data_items:
                a = "<tr><td>%s</td>" % i[0]
                answer.append(a)
                a1 = "<td>%s</td>" % i[1]
                answer.append(a1)
                a2 = "<td>%s</td>" % i[2]
                answer.append(a2)
                a3 = "<td>%s</td>" % i[3]
                answer.append(a3)
                a4 = "<td>%s</td>" % i[4]
                answer.append(a4)
                a5 = "<td>%s</td>" % i[5]
                answer.append(a5)
                a6 = "<td>%s</td>" % i[6]
                answer.append(a6)
                a7 = "<td>%s</td>" % i[7]
                answer.append(a7)
                a8 = "<td>%s</td></tr>" % i[8]
                answer.append(a8)
            answer1[count] = answer
            idx[count] = idxcount
            count += 1
        else:
            c2 += 1
   # print(idx)
    if f == 0:
        print("No period assigned")
    c1.name = c1.name
    contents = '''<!DOCTYPE html>
            <html>
            <head>
            <meta content = "text/html; charset = UTF-8"
            http-equip = "content-type">
            <style>
            td {
                padding :0 15px;
            }
            </style>
            <title>Time Table</title>
            </head>
            <body>
                <center>
                <div class="card" id="generatePDF">
            <center>
            <div class="card" id="generatePDF">
            <br><br>
         
            <center>
            <h3>%s</h3>
            <table border = 1>
            %s
            </table>
            </center>
            <br><br>
            
            <center>
            <h3>%s</h3>
            <table border = 1>
            %s
            </table>
            </center>
            <br><br>
           
           <center>
           <h3>%s</h3>
            <table border = 1>
            %s
            </table>
            </center>
            <br><br>
            
            <center>
            <h3>%s</h3>
            <table border = 1>
            %s
            </table>
            </center>
            
     <button id="pdfButton"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzxA1IZaV_fN96xiySAwgY5iZiM-pIg9W9ig&usqp=CAU" style="height:30px;width:30px;"><b style="padding-bottom:5px;" class="text"> <center>&nbsp; &nbsp Download</center></b></button>
  
  </div>
  </center>
     <script>
      var button = document.getElementById("pdfButton");
      var makepdf = document.getElementById("generatePDF");
      button.addEventListener("click", function () {
         var mywindow = window.open("", "PRINT", "height=600,width=600");
         mywindow.document.write(makepdf.innerHTML);
         mywindow.document.close();
         mywindow.focus();
         mywindow.print();
         return true;
      });
   </script>
            </body>
            </html>
            '''%(answer2[0], answer1[0],answer2[1],answer1[1],answer2[2],answer1[2],answer2[3], answer1[3])

    filename = 'demo1.html'
    def main(contents,filename):
        output = open(filename,"w")
        output.write(contents)
        output.close()
    main(contents,filename)
    webbrowser.open(filename)
    
    return render_template('demo1.html', n1 = c1.name, n2 = ans) 

@app.route('/submission')
def submission():
    return render_template('submission.html')

@app.route('/Registration')
def Registration():
    return render_template('Registration.html')

@app.route('/', methods = ['POST'])
def run_script():
    file = open(r'C:\Users\Harshita\Downloads\time\timetabledemp.py', 'r').read()
    return exec(file)
    


app.run(debug = True)
login()
getvalue()
preferences()
getName()