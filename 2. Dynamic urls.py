from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
# This lets us to pass a username into the url
def show_user(username):
    # Greet the user
    return f'Hello {username} !'

# Pass the required route to the decorator.
@app.route("/hello/<username>")
def hello(username):
    # Greet the user
    return f"Hello, Welcome {username}"
  
@app.route("/")
def index():
    # Return the homepage
    return "Homepage"

if __name__ == "__main__":
    app.run(debug=True)