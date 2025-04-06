from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!\n" + "<a href='/about'>About</a>" + "\n" + "<a href='/users'>Users</a>"

@app.route('/about')
def about():
    return 'To ja i o mnie.'

@app.route('/users')
def users():
    users = {1: {"name": "Ala", "age": 22}, 2: {"name": "Bartek", "age": 25}, 3: {"name": "Celina", "age": 30}}
    return [users[id]['name'] for id in users]

@app.route('/users/<int:id>')
def user(id):
    users = {1: {"name": "Ala", "age": 22}, 2: {"name": "Bartek", "age": 25}, 3: {"name": "Celina", "age": 30}}
    if id in users:
        return users[id]
    else:
        return "Uzytkownik nie istnieje."


if __name__ == "__main__":

    app.run(debug=True)
