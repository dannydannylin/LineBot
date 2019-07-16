from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hi web!!"

@app.route("/test", methods=['GET', 'POST'])
def test():
    return "Hi test!!"

if __name__ == "__main__":
    app.run()