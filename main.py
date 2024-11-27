# app.py
from flask import Flask

from controllers.medicine import medicine_blueprint
from controllers.medicine_package import medicine_package_blueprint
from controllers.package_type import package_type_blueprint

app = Flask(__name__)

# Register the user blueprint
app.register_blueprint(medicine_blueprint)
app.register_blueprint(package_type_blueprint)
app.register_blueprint(medicine_package_blueprint)


@app.route('/')
def index():
    return "Welcome to the Flask app with Blueprints!", 200


if __name__ == '__main__':
    app.run(debug=True)
