from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi web!!"

@app.route("/test")
def test():
    return "Hi test!!"

if __name__ == "__main__":
    app.run()