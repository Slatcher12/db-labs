from flask import Flask
from controllers.medicine import medicine_blueprint
from controllers.category import category_blueprint
from controllers.manufacturer import manufacturer_blueprint

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(medicine_blueprint, url_prefix='/api')
app.register_blueprint(category_blueprint, url_prefix='/api')
app.register_blueprint(manufacturer_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
