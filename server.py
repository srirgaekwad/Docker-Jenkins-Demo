from flask import Flask

PORT = 8000
MESSAGE = "Hello My Name is Srinath R Gaekwad and This is my Project for Submission \n"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
