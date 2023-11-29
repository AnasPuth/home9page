from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# User database (in memory, replace this with a database in a real application)
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # Redirect to the user's profile page after successful login
            return redirect(url_for('user_profile', username=username))
        else:
            # Incorrect username or password
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html', error=None)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('signup.html', error='Username already exists')
        else:
            # Add the new user to the database (in memory, replace this with a database in a real application)
            users[username] = password
            # Redirect to the user's profile page after successful signup
            return redirect(url_for('user_profile', username=username))
    return render_template('signup.html', error=None)

@app.route('/user/<username>')
def user_profile(username):
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
