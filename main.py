from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/python')
def python():
    return render_template('python.html')

@app.route('/poo')
def poo():
    return render_template('poo.html')

if __name__ == "__main__":
    app.run(debug=True)