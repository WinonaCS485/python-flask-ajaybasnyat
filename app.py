from flask import Flask, render_template
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='fx9785rk',
                             password='Pernambucano.wolf',
                             db='fx9785rk_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT StudentID, FirstName, LastName from Student"
        
        # execute the SQL command
        cursor.execute(sql)

        studentList = ""

        for student in cursor:
            studentList = studentList + str(student) + "<br>"

finally:
    connection.close()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/students')
def students():
    return  studentList

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9785)