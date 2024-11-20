from flask import Blueprint, request, jsonify
from services.manufacturer import (
    create_manufacturer,
    get_all_manufacturers,
    get_manufacturer_by_id,
    update_manufacturer,
    delete_manufacturer,
)

manufacturer_blueprint = Blueprint('manufacturer', __name__)

@manufacturer_blueprint.route('/', methods=['POST'])
def create():
    data = request.json
    manufacturer = create_manufacturer(data)
    return jsonify({
        "id": manufacturer.id,
        "name": manufacturer.name,
        "address": manufacturer.address,
        "contact_info": manufacturer.contact_info,
        "medicine_id": manufacturer.medicine_id
    }), 201

@manufacturer_blueprint.route('/', methods=['GET'])
def get_all():
    manufacturers = get_all_manufacturers()
    return jsonify([{
        "id": m.id,
        "name": m.name,
        "address": m.address,
        "contact_info": m.contact_info,
        "medicine_id": m.medicine_id
    } for m in manufacturers]), 200

@manufacturer_blueprint.route('/<int:manufacturer_id>', methods=['GET'])
def get_one(manufacturer_id):
    manufacturer = get_manufacturer_by_id(manufacturer_id)
    if not manufacturer:
        return jsonify({"error": "Manufacturer not found"}), 404
    return jsonify({
        "id": manufacturer.id,
        "name": manufacturer.name,
        "address": manufacturer.address,
        "contact_info": manufacturer.contact_info,
        "medicine_id": manufacturer.medicine_id
    }), 200

@manufacturer_blueprint.route('/<int:manufacturer_id>', methods=['PUT'])
def update(manufacturer_id):
    data = request.json
    manufacturer = update_manufacturer(manufacturer_id, data)
    if not manufacturer:
        return jsonify({"error": "Manufacturer not found"}), 404
    return jsonify({
        "id": manufacturer.id,
        "name": manufacturer.name,
        "address": manufacturer.address,
        "contact_info": manufacturer.contact_info,
        "medicine_id": manufacturer.medicine_id
    }), 200

@manufacturer_blueprint.route('/<int:manufacturer_id>', methods=['DELETE'])
def delete(manufacturer_id):
    manufacturer = delete_manufacturer(manufacturer_id)
    if not manufacturer:
        return jsonify({"error": "Manufacturer not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
