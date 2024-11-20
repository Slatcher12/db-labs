from models.medicine import Medicine
from models.session import db_session
from schemas.medicine import MedicineSchema

def create_medicine(data):
    """Створити новий лікарський засіб."""
    new_medicine = Medicine(**data)
    db_session.add(new_medicine)
    db_session.commit()
    return MedicineSchema(new_medicine).to_dict()

def get_all_medicines():
    """Отримати всі лікарські засоби."""
    medicines = db_session.query(Medicine).all()
    return [MedicineSchema(medicine).to_dict() for medicine in medicines]

def get_medicine_by_id(medicine_id):
    """Отримати лікарський засіб за ID."""
    medicine = db_session.query(Medicine).filter(Medicine.id == medicine_id).first()
    return MedicineSchema(medicine).to_dict() if medicine else None

def update_medicine(medicine_id, data):
    """Оновити лікарський засіб."""
    medicine = db_session.query(Medicine).filter(Medicine.id == medicine_id).first()
    if medicine:
        for key, value in data.items():
            setattr(medicine, key, value)
        db_session.commit()
        return MedicineSchema(medicine).to_dict()
    return None

def delete_medicine(medicine_id):
    """Видалити лікарський засіб."""
    medicine = db_session.query(Medicine).filter(Medicine.id == medicine_id).first()
    if medicine:
        db_session.delete(medicine)
        db_session.commit()
        return MedicineSchema(medicine).to_dict()
    return None
