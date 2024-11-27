from flask import Blueprint, jsonify, request
from services.medicine import MedicinesService
from schemas.medicine import MedicineDTO, CreateMedicineDTO

# Define the blueprint: 'medicine', set its url prefix: /medicines
medicine_blueprint = Blueprint('medicines', __name__, url_prefix='/medicines')


@medicine_blueprint.get("/")
def get_all_medicines():
    medicines = MedicinesService.get_all_medicines()
    response = [MedicineDTO.model_validate(medicine.__dict__).model_dump() for medicine in medicines]
    return jsonify(response)


@medicine_blueprint.get("/<int:id>")
def get_medicine(id: int):
    medicine = MedicinesService.get_medicine_by_id(id=id)
    response = MedicineDTO.model_validate(medicine.__dict__).model_dump()
    return jsonify(response)


@medicine_blueprint.post("/")
def create_medicine():
    body = CreateMedicineDTO.model_validate(request.get_json())
    medicine = MedicinesService.create_medicine(
        name=body.name,
        description=body.description,
    )
    response = MedicineDTO.model_validate(medicine.__dict__).model_dump()
    return jsonify(response)


@medicine_blueprint.put("/<int:id>")
def update_medicine(id: int):
    body = CreateMedicineDTO.model_validate(request.get_json())
    medicine = MedicinesService.update_medicine(
        id=id,
        name=body.name,
        description=body.description,
    )
    response = MedicineDTO.model_validate(medicine.__dict__).model_dump()
    return jsonify(response)


@medicine_blueprint.delete("/<int:id>")
def delete_medicine(id: int):
    MedicinesService.delete_medicine(id=id)
    return jsonify({"detail": "medicine deleted successfully"})