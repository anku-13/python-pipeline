from flask import Flask

app = Flask(__name__)

@app.route("/")
def add(first_term, second_term):
    return first_term + second_term


if __name__ == "__main__":
    app.run()
