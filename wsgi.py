from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! This is B app! v.2.0."

if __name__ == "__main__":
    application.run()
