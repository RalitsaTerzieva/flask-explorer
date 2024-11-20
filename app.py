from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    puppy_information = [
        {'name': 'Bliss', 'age': 2, 'breed': 'Golden Retriever', 'image': 'golden.jpg'},
        {'name': 'Max', 'age': 3, 'breed': 'Bulldog', 'image': 'bulldog.jpg'},
        {'name': 'Bella', 'age': 1, 'breed': 'Beagle', 'image': 'beagle.jpg'},
        {'name': 'Rocky', 'age': 4, 'breed': 'German Shepherd', 'image': 'germanshepherd.jpg'}
    ]
     
    return render_template("home.html", puppy_information=puppy_information)

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1>"

@app.route('/puppy/<name>')
def puppy(name):
    return render_template('puppy.html', name=name)

@app.route('/puppy_latin/<name>')
def puppy_name(name):
    if name[-1] != 'y':
        return f"Hi, {name.capitalize()}! puppylatin name is {name.capitalize()}y"
    else:
        return f"Hi, {name.capitalize()}y! Your puppylatin name is {name[:-1].capitalize()}iful"

if __name__ == "__main__":
    app.run(debug=True)

