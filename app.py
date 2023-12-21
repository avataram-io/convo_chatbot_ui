from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/forget_pass')
def forget_pass():
    return render_template('forgot-password.html')

@app.route('/table')
def table():
    return render_template('tables.html')


if __name__ == '__main__':
    app.run(debug=True)