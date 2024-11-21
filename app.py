from flask import Flask, render_template, request

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

@app.route('/signup_form')
def signup_form():
    return render_template("signup.html")

@app.route('/thank-you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template("thankyou.html", first=first, last=last)

@app.route('/puppy/<name>')
def puppy(name):
    return render_template('puppy.html', name=name)

@app.route('/puppy_latin/<name>')
def puppy_name(name):
    if name[-1] != 'y':
        return f"Hi, {name.capitalize()}! puppylatin name is {name.capitalize()}y"
    else:
        return f"Hi, {name.capitalize()}y! Your puppylatin name is {name[:-1].capitalize()}iful"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)

