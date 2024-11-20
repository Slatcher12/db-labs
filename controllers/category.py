from flask import Blueprint, request, jsonify
from services.category import (
    create_category,
    get_all_categories,
    get_category_by_id,
    update_category,
    delete_category,
)

category_blueprint = Blueprint('category', __name__)

@category_blueprint.route('/', methods=['POST'])
def create():
    """
    Створити нову категорію.
    """
    data = request.json
    try:
        category = create_category(data)
        return jsonify({
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "medicine_id": category.medicine_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@category_blueprint.route('/', methods=['GET'])
def get_all():
    """
    Отримати список усіх категорій.
    """
    categories = get_all_categories()
    return jsonify([{
        "id": c.id,
        "name": c.name,
        "description": c.description,
        "medicine_id": c.medicine_id
    } for c in categories]), 200

@category_blueprint.route('/<int:category_id>', methods=['GET'])
def get_one(category_id):
    """
    Отримати категорію за її ID.
    """
    category = get_category_by_id(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    return jsonify({
        "id": category.id,
        "name": category.name,
        "description": category.description,
        "medicine_id": category.medicine_id
    }), 200

@category_blueprint.route('/<int:category_id>', methods=['PUT'])
def update(category_id):
    """
    Оновити дані категорії за її ID.
    """
    data = request.json
    try:
        category = update_category(category_id, data)
        if not category:
            return jsonify({"error": "Category not found"}), 404
        return jsonify({
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "medicine_id": category.medicine_id
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@category_blueprint.route('/<int:category_id>', methods=['DELETE'])
def delete(category_id):
    """
    Видалити категорію за її ID.
    """
    try:
        category = delete_category(category_id)
        if not category:
            return jsonify({"error": "Category not found"}), 404
        return jsonify({"message": "Deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
