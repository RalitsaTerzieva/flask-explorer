from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, puppy!</h1>"

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return "<h1>This is {}</h1>".format(name[100])

@app.route('/puppy_latin/<name>')
def puppy_name(name):
    if name[-1] != 'y':
        return f"Hi, {name.capitalize()}! puppylatin name is {name.capitalize()}y"
    else:
        return f"Hi, {name.capitalize()}y! Your puppylatin name is {name[:-1].capitalize()}iful"

if __name__ == "__main__":
    app.run(debug=True)

