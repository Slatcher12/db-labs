from flask import Blueprint, request, jsonify
from services.medicine import create_medicine, get_all_medicines, get_medicine_by_id, delete_medicine

medicine_blueprint = Blueprint('medicine', __name__)

@medicine_blueprint.route('/medicines', methods=['POST'])
def create():
    data = request.json
    medicine = create_medicine(data)
    return jsonify({"id": medicine.id, "name": medicine.name}), 201

@medicine_blueprint.route('/medicines', methods=['GET'])
def get_all():
    medicines = get_all_medicines()
    return jsonify([{"id": m.id, "name": m.name} for m in medicines]), 200

@medicine_blueprint.route('/medicines/<int:medicine_id>', methods=['GET'])
def get_one(medicine_id):
    medicine = get_medicine_by_id(medicine_id)
    if not medicine:
        return jsonify({"error": "Medicine not found"}), 404
    return jsonify({"id": medicine.id, "name": medicine.name}), 200

@medicine_blueprint.route('/medicines/<int:medicine_id>', methods=['DELETE'])
def delete(medicine_id):
    medicine = delete_medicine(medicine_id)
    if not medicine:
        return jsonify({"error": "Medicine not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
