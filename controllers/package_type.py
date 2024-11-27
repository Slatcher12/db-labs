from flask import Blueprint, jsonify, request
from services.package_type import PackageTypesService
from schemas.package_type import PackageTypeDTO, CreatePackageTypeDTO

# Define the blueprint: 'package_type', set its url prefix: /package_types
package_type_blueprint = Blueprint('package_types', __name__, url_prefix='/package_types')


@package_type_blueprint.get("/")
def get_all_package_types():
    package_types = PackageTypesService.get_all_package_types()
    response = [PackageTypeDTO.model_validate(package_type.__dict__).model_dump() for package_type in package_types]
    return jsonify(response)


@package_type_blueprint.get("/<int:id>")
def get_package_type(id: int):
    package_type = PackageTypesService.get_package_type_by_id(id=id)
    response = PackageTypeDTO.model_validate(package_type.__dict__).model_dump()
    return jsonify(response)


@package_type_blueprint.post("/")
def create_package_type():
    body = CreatePackageTypeDTO.model_validate(request.get_json())
    package_type = PackageTypesService.create_package_type(
        type=body.type,
        description=body.description
    )
    response = PackageTypeDTO.model_validate(package_type.__dict__).model_dump()
    return jsonify(response)


@package_type_blueprint.put("/<int:id>")
def update_package_type(id: int):
    body = CreatePackageTypeDTO.model_validate(request.get_json())
    package_type = PackageTypesService.update_package_type(
        id=id,
        type=body.type,
        description=body.description
    )
    response = PackageTypeDTO.model_validate(package_type.__dict__).model_dump()
    return jsonify(response)


@package_type_blueprint.delete("/<int:id>")
def delete_package_type(id: int):
    PackageTypesService.delete_package_type(id=id)
    return jsonify({"detail": "package type deleted successfully"})