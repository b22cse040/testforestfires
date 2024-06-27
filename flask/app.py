from flask import Flask, render_template

'''
    It creates an instance of the Flask class,
    which will be your WSGI application.
'''

#WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
  return "<html><h1>Welcome to this website. I am learning Flask!</h1></html>"

@app.route("/index", methods = ['GET'])
def index():
  return render_template('index.html')

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.run(debug = True)