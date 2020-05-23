from flask import Flask, render_template, redirect, request, url_for 


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

    
@app.route('/poem')
def poem():
    return render_template('poems.html')


if __name__ == '__main__':
    app.run(debug=True)

