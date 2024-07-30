from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the technical session, humans!!'

@app.route('/health')
def health():
    return 'Server is up and running'