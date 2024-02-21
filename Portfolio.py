from flask import Flask, render_template

app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    return render_template('intro.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/stockpreview')
def stockpreview():
    return render_template('stockpreview.html')

@app.route('/monthlypreview')
def monthlypreview():
    return render_template('monthlypreview.html')

if __name__ == '__main__':
    app.run(debug=True)
