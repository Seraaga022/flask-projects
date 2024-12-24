from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.txt', un = name)

@app.errorhandler(404)
def pageNotFound(e):
    return '<h1><center> 404 </center> </h1>  <h1> <center>page not found, URL essue ..</center> </h1>'

if __name__ == '__main__':
    app.run (debug = True, host = '0.0.0.0', port = 80)