from flask import Flask
from controllers.medicine import medicine_blueprint
from controllers.category import category_blueprint
from controllers.manufacturer import manufacturer_blueprint
from config.app import init_db

# Створення Flask-додатка
app = Flask(__name__)

# Ініціалізація бази даних
init_db()

# Реєстрація маршрутів (blueprints)
app.register_blueprint(medicine_blueprint, url_prefix='/api/medicines')
app.register_blueprint(category_blueprint, url_prefix='/api/categories')
app.register_blueprint(manufacturer_blueprint, url_prefix='/api/manufacturers')

# Головний маршрут
@app.route('/')
def index():
    return {"message": "Welcome to the Flask API for managing medicines!"}, 200

if __name__ == '__main__':
    app.run(debug=True)
