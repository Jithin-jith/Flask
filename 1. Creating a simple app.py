from flask import Flask

app = Flask(__name__)

@app.route('/hello')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'
# The hello function is now mapped with the "/hello" path and we get the output of the function rendered on the browser.

@app.route("/")
def index():
    return "Homepage"

# The index function is now mapped with the "/" path and we get the output of the function rendered on the browser.

# main driver function
if __name__ == '__main__':

    app.run()
