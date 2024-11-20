from models.manufacturer import Manufacturer
from models.session import db_session
from schemas.manufacturer import ManufacturerSchema

def create_manufacturer(data):
    """Створити нового виробника."""
    new_manufacturer = Manufacturer(**data)
    db_session.add(new_manufacturer)
    db_session.commit()
    return ManufacturerSchema(new_manufacturer).to_dict()

def get_all_manufacturers():
    """Отримати всіх виробників."""
    manufacturers = db_session.query(Manufacturer).all()
    return [ManufacturerSchema(manufacturer).to_dict() for manufacturer in manufacturers]

def get_manufacturer_by_id(manufacturer_id):
    """Отримати виробника за ID."""
    manufacturer = db_session.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()
    return ManufacturerSchema(manufacturer).to_dict() if manufacturer else None

def update_manufacturer(manufacturer_id, data):
    """Оновити дані виробника."""
    manufacturer = db_session.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()
    if manufacturer:
        for key, value in data.items():
            setattr(manufacturer, key, value)
        db_session.commit()
        return ManufacturerSchema(manufacturer).to_dict()
    return None

def delete_manufacturer(manufacturer_id):
    """Видалити виробника."""
    manufacturer = db_session.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).first()
    if manufacturer:
        db_session.delete(manufacturer)
        db_session.commit()
        return ManufacturerSchema(manufacturer).to_dict()
    return None
