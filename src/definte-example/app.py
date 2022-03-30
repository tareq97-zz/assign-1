from flask import Flask
from flask import render_template

app = Flask(__name__)

#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"@app.route('/hello/')

@app.route('/')
@app.route('/app/')
@app.route('/app/<name>')
def application(name=None):
    return render_template('base.html', name=name)

@app.route('/app/first')
def first():
    return render_template('first.html')

@app.route('/app/second')
def second():
    return render_template('second.html')

@app.route('/app/third')
def third():
    return render_template('third.html')

@app.route('/app/fourth')
def fourth():
    return render_template('fourth.html')

@app.route('/app/fifth')
def fifth():
    return render_template('fifth.html')

@app.route('/app/sixth')
def sixth():
    return render_template('sixth.html')

@app.route('/app/seventh')
def seventh():
    return render_template('seventh.html')

@app.route('/app/eight')
def eight():
    return render_template('eight.html')

@app.route('/app/nine')
def nine():
    return render_template('nine.html')

@app.route('/app/ten')
def ten():
    return render_template('ten.html')

#if __name__ == "__main__":
#    app.run(debug=True)

