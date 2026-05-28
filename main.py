from flask import Flask, Blueprint

app = Flask(__name__)

views = Blueprint("views", __name__)
@views.route("/")
def home():
    return "Home"

app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)