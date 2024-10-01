import mysql
from flask import render_template, Flask, request, redirect, url_for

from flask_mysqldb import MySQL
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='Students1'
row=[]
city=''

mysql=MySQL(app)

@app.route('/Lecture',methods=['POST','GET'])
def Lecture():
    msg=''
    if request.method=='GET':
        return render_template('Lectures.html',msg=msg)
    if request.method=='POST':
        LectureId = request.form['LectureId']
        LectureName = request.form['LectureName']
        Password = request.form['Password']
        ConformPassword = request.form['ConformPassword']
        Course = request.form['Course']

        cursor=mysql.connection.cursor()
        cursor.execute('''INSERT INTO Lecture VALUES(%s,%s,%s,%s,%s)''', (LectureId,LectureName,Password,ConformPassword,Course))
        mysql.connection.commit()
        cursor.close()
    return render_template('Lectures.html')

@app.route('/Course',methods=['POST','GET'])
def Course():
    msg=''
    if request.method=='GET':
        return render_template('Course.html',msg=msg)
    if request.method=='POST':
        CourseId = request.form['CourseId']
        CourseName = request.form['CourseName']
        Comment = request.form['Comment']
        CourseKey = request.form['CourseKey']

        cursor=mysql.connection.cursor()
        cursor.execute('''INSERT INTO Course VALUES(%s,%s,%s,%s)''', (CourseId,CourseName,Comment,CourseKey))
        mysql.connection.commit()
        cursor.close()
    return render_template('Course.html')

@app.route('/Subject',methods=['POST','GET'])
def Subject():
    msg=''
    if request.method=='GET':
        return render_template('Subject.html',msg=msg)
    if request.method=='POST':
        SubjectId = request.form['SubjectId']
        SubjectName = request.form['SubjectName']
        Comment = request.form['Comment']
        Course = request.form['Course']

        cursor=mysql.connection.cursor()
        cursor.execute('''INSERT INTO Subject VALUES(%s,%s,%s,%s)''', (SubjectId,SubjectName,Comment,Course))
        mysql.connection.commit()
        cursor.close()
    return render_template('Subject.html')

@app.route('/Student',methods=['POST','GET'])
def Student():
    msg=''
    if request.method=='GET':
        return render_template('Student.html',msg=msg)
    if request.method=='POST':
        StudentId = request.form['StudentId']
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        DOB = request.form['DOB']
        #Gender = request.form['Gender']
        FatherName = request.form['FatherName']
        Address = request.form['Address']
        ContactNo = request.form['ContactNo']
        Course = request.form['Course']
        Semester = request.form['Semester']

        cursor=mysql.connection.cursor()
        cursor.execute('''INSERT INTO Student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (StudentId,FirstName,LastName,DOB,FatherName,Address,ContactNo,Course,Semester))
        mysql.connection.commit()
        cursor.close()
    return render_template('Student.html')


@app.route('/DeleteLecture/<string:id_data>', methods=['GET'])
def DeleteLecture(id_data):
    msg=''
    print(id_data)

    LectureId= id_data #request.form['LectureId']
    cur = mysql.connection.cursor()
    print(id_data)
    cur.execute("DELETE FROM Lecture WHERE LectureId=%s",(id_data,))
    mysql.connection.commit()

    return redirect(url_for('ViewLecture'))

@app.route('/DeleteCourse', methods=['POST','GET'])
def DeleteCourse():
    msg=''
    if request.method=='GET':
        return render_template('Course.html',msg=msg)
    if request.method=='POST':
        CourseId= request.form['CourseId']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Course WHERE CourseId=%s",(CourseId,))
        mysql.connection.commit()

    return render_template('Course.html')

@app.route('/DeleteSubject', methods=['POST','GET'])
def DeleteSubject():
    msg=''
    if request.method=='GET':
        return render_template('Subject.html',msg=msg)
    if request.method=='POST':
        SubjectId= request.form['SubjectId']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Subject WHERE SubjectId=%s",(SubjectId,))
        mysql.connection.commit()

    return render_template('Subject.html')

@app.route('/DeleteStudent', methods=['POST','GET'])
def DeleteStudent():
    msg=''
    if request.method=='GET':
        return render_template('Student.html',msg=msg)
    if request.method=='POST':
        StudentId= request.form['StudentId']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Student WHERE StudentId=%s",(StudentId,))
        mysql.connection.commit()

    return render_template('Student.html')

@app.route('/UpdateLecture', methods=['POST','GET'])
def UpdateLecture():
    msg=''
    print("req ", request.method)
    if request.method=='GET':
        return render_template('Lectures.html',msg=msg)

    if request.method=='POST':
        LectureId = request.form['LectureId']
        LectureName = request.form['LectureName']
        Password = request.form['Password']
        ConformPassword = request.form['ConformPassword']
        Course = request.form['Course']

        cur = mysql.connection.cursor()
        cur.execute("SET SQL_SAFE_UPDATES=0")
        cur.execute("update lecture set LectureName=%s,Password=%s,ConformPassword=%s,Course=%s WHERE LectureId=%s",(LectureName, Password, ConformPassword, Course,LectureId))
        mysql.connection.commit()
    return redirect(url_for('ViewLecture'))

@app.route('/UpdateCourse', methods=['POST','GET'])
def UpdateCourse():
    msg=''
    if request.method=='GET':
        return render_template('Course.html',msg=msg)
    if request.method=='POST':
        CourseId = request.form['CourseId']
        CourseName = request.form['CourseName']
        Comment = request.form['Comment']
        CourseKey = request.form['CourseKey']

        cur = mysql.connection.cursor()
        cur.execute("SET SQL_SAFE_UPDATES=0")
        cur.execute("update Course set CourseName=%s,Comment=%s,CourseKey=%s WHERE CourseId=%s",(CourseName, Comment, CourseKey,CourseId))
        mysql.connection.commit()


    return redirect(url_for('ViewCourse'))

@app.route('/UpdateSubject', methods=['POST','GET'])
def UpdateSubject():
    msg=''
    if request.method=='GET':
        return render_template('Subject.html',msg=msg)
    if request.method=='POST':
        SubjectId = request.form['SubjectId']
        SubjectName = request.form['SubjectName']
        Comment = request.form['Comment']
        Course = request.form['Course']

        cur = mysql.connection.cursor()
        cur.execute("SET SQL_SAFE_UPDATES=0")
        cur.execute("update Subject set SubjectName=%s,Comment=%s,Course=%s WHERE SubjectId=%s",(SubjectName, Comment, Course,SubjectId))
        mysql.connection.commit()
    return redirect(url_for('ViewSubject'))

@app.route('/UpdateStudent', methods=['POST','GET'])
def UpdateStudent():
    msg=''
    print("req ", request.method)
    if request.method=='GET':
        return render_template('Student.html',msg=msg)
    if request.method=='POST':
        StudentId = request.form['StudentId']
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        DOB = request.form['DOB']

        FatherName = request.form['FatherName']
        Address = request.form['Address']
        ContactNo = request.form['ContactNo']
        Course = request.form['Course']
        Semester = request.form['Semester']

        cur = mysql.connection.cursor()
        cur.execute("SET SQL_SAFE_UPDATES=0")

        cur.execute("update Student set StudentId=%s,LastName=%s,DOB=%s,FatherName=%s,Address=%s,ContactNo=%s,Course=%s,Semester=%s WHERE FirstName=%s",(StudentId, LastName, DOB, FatherName, Address, ContactNo, Course, Semester, FirstName))
        mysql.connection.commit()
    return redirect(url_for('ViewStudent'))

@app.route('/ViewLecture', methods=['POST','GET'])
def ViewLecture():

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Lecture')
        users = cur.fetchall()
        return render_template('Lectures table.html', users=users)

@app.route('/ViewSubject', methods=['POST','GET'])
def ViewSubject():

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Subject')
        users = cur.fetchall()
        return render_template('Subject table.html', users=users)

@app.route('/ViewStudent', methods=['POST','GET'])
def ViewStudent():

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Student')
        users = cur.fetchall()
        return render_template('Student table.html', users=users)

@app.route('/ViewCourse', methods=['POST','GET'])
def ViewCourse():

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM Course')
        users = cur.fetchall()
        return render_template('Course table.html', users=users)










if __name__=='__main__':
    app.run(port=5000,debug = True)
