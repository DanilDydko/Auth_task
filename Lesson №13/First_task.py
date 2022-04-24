from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/second')
def second():
    return "The second breakpoint"

if __name__ == '__main__':
    app.run()
