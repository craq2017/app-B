from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! This is B v7.77 app!! Yay!!!"

if __name__ == "__main__":
    application.run()
