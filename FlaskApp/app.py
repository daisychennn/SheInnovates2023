from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return 'hello'

if __name__== 'main':
    app.run(debug=True, port=5001)