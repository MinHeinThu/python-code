from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a random key in production

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gmail = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/account')
def account():
    user_id = session.get('user_id')
    user = None
    if user_id:
        user = User.query.get(user_id)
    return render_template('account.html', user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        gmail = request.form['gmail']
        password = request.form['password']

        # Check if user already exists
        if User.query.filter_by(gmail=gmail).first():
            flash("An account with this email already exists.", "warning")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(name=name, gmail=gmail, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Log in the new user
        session['user_id'] = new_user.id
        flash("Account created! You are now logged in.", "success")
        return redirect(url_for('account'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        gmail = request.form['gmail']
        password = request.form['password']
        user = User.query.filter_by(gmail=gmail).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash(f"Welcome back, {user.name}!", "success")
            return redirect(url_for('account'))
        else:
            flash("Incorrect email or password.", "danger")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)