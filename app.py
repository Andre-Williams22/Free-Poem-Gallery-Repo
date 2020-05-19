from flask import Flask, render_template, redirect, request, url_for 



app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/home_two')
def home_two():
    # update 
    return render_template('hometwo.html')

if __name__ == '__main__':
    app.run(debug=True)

