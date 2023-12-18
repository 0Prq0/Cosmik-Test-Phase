from flask import Flask,render_template,redirect,request, session
import db

app = Flask(__name__)

@app.route('/')
def home():
 return render_template('sign up.html')

@app.errorhandler(404)
def not_found(e):
 return render_template('404.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')