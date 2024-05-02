from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'neetnav123',
    'database': 'gym_users'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        dob = request.form['dob']
        age = request.form['age']
        feet = request.form['feet']
        inches = request.form['inches']
        weight = request.form['weight']
        need_trainer = request.form['needTrainer']
        trained_before = request.form['trainedBefore']
        train_time = request.form['trainTime']

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insert data into the database
        sql = "INSERT INTO users (first_name, last_name, email, phone, gender, dob, age, feet, inches, weight, need_trainer, trained_before, train_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (first_name, last_name, email, phone, gender, dob, age, feet, inches, weight, need_trainer, trained_before, train_time)
        cursor.execute(sql, values)

        # Commit changes and close connection
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
