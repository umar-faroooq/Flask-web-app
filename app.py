from flask import Flask


app = Flask(__name__)



@app.route("/")
def home():
    return "Hello, World! of codes"


if __name__=="__main__":
    app.run(debug=True)