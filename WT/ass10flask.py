from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Greeting App! Append your name in the URL like /yourname"

@app.route('/<username>')
def greet_user(username):
    return f"Hello, {username.capitalize()}! Welcome to our Flask App."

if __name__ == '__main__':
    app.run(debug=True)
