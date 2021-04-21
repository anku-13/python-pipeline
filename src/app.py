from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    x=input()
    y=input()
    print(x+y)
    return "Hello World"


if __name__ == "__main__":
    app.run()
