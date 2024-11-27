from flask import Blueprint, jsonify, request

from services.medicine_package import MedicinePackagesService
from schemas.medicine_package import MedicinePackageDTO, CreateMedicinePackageDTO

# Define the blueprint: 'medicine_package', set its url prefix: /medicine_packages
medicine_package_blueprint = Blueprint('medicine_packages', __name__, url_prefix='/medicine_packages')


@medicine_package_blueprint.get("/")
def get_all_medicine_packages():
    medicine_packages = MedicinePackagesService.get_all_medicine_packages()
    response = [MedicinePackageDTO.model_validate(medicine_package).model_dump() for medicine_package in medicine_packages]
    return jsonify(response)


@medicine_package_blueprint.get("/<int:id>")
def get_medicine_package(id: int):
    medicine_package = MedicinePackagesService.get_medicine_package_by_id(id=id)
    if not medicine_package:
        return jsonify({"detail": "Medicine package not found"}), 404
    response = MedicinePackageDTO.model_validate(medicine_package).model_dump()
    return jsonify(response)


@medicine_package_blueprint.post("/")
def create_medicine_package():
    body = CreateMedicinePackageDTO.model_validate(request.get_json())
    medicine_package = MedicinePackagesService().create_medicine_package(
        medicine_id=body.medicine_id,
        package_type_id=body.package_type_id,
        quantity=body.quantity
    )
    response = MedicinePackageDTO.model_validate(medicine_package).model_dump()
    return jsonify(response)


@medicine_package_blueprint.put("/<int:id>")
def update_medicine_package(id: int):
    body = CreateMedicinePackageDTO.model_validate(request.get_json())
    medicine_package = MedicinePackagesService().update_medicine_package(
        id=id,
        medicine_id=body.medicine_id,
        package_type_id=body.package_type_id,
        quantity=body.quantity
    )
    response = MedicinePackageDTO.model_validate(medicine_package).model_dump()
    return jsonify(response)


@medicine_package_blueprint.delete("/<int:id>")
def delete_medicine_package(id: int):
    MedicinePackagesService.delete_medicine_package(id=id)
    return jsonify({"detail": "medicine package deleted successfully"})