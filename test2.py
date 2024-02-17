 from flask import Flask 
from flask import Flask 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world() :
 return "<h1>Hello, World!</h1>"

@app.route("/")
def hello_world() :
 return "<h1>Hello, World!</h1>"

@app.route("/")
def hello_world () :
 return "<h1>Hello, World!<h1>"

@app.route("/")
def hello_world() :
 return "<h1>Hello, World!</h1>"
 return "<h1>Hello, World!</h1>"

@app.route("/hello_world1")
def hello_world1() :
 return "<h1>Hello, World!2</h1>"

@app.route("/Hello_world")
def hello_world() :
 return "<h1>Hello ,world!</h1>"

@app.route("/hello_world3")
def hello_world3() :
 return "<h1>Hello , World!3</h1>"

@app.route("/hello_world3")
def hello_world () :
 return "<h1>Hello, World!3</h1>"
 return "<h1>Hello , World!3</h1>"

@app.route ("/hello_world2")
def hello_world2 () :
 return "<h1>Hello, World!2</h1>"

@app.route ("/hello_world2") 
def hello_world2 () :
 return "<h1>Hello , World!2</h1>"

@app.route("/test")
def test () :
 a = 5 +_6 
 return "this is my function to run app {}".format(a)

@app.route("/hello_world2")
@app.route("/test")
def test () :
 return "this is  a data function to run app {}".format(a)

@app.route("/test") 
def test () :
 return "this is a data function to run app {}".format(a)

@app.route("/test2/test2")
def test2 () :
 data = request.args.get("x")
 return "this is my data input form my url {}".format(data)

@app.route ("/test2/test2/")
def test2() :
 data = request.args.get('x')
 return "this is my data input form my url {}".format(data)

if __name__== "__main__" :
 app.run(host="0.0.0.0")