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

@app.route('/temp')
def temp():
    return render_template('temp.html')

# @app.route('/change_pass')
# def change_pass():
#     return render_template('change-password.html')

@app.route('/tableintent')
def tableintent():
    # return render_template('temp.html')
    return render_template('tableintent.html')

@app.route('/tablequestion')
def tablequestion():
    return render_template('tablequestion.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')