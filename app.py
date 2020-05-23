from flask import Flask, render_template, redirect, request, url_for 


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

    
@app.route('/poem', methods=['GET', 'POST'])
def poem():
    return render_template('poems.html')


if __name__ == '__main__':
    app.run(debug=True)

