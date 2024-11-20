from models.category import Category
from models.session import db_session
from schemas.category import CategorySchema

def create_category(data):
    """Створити нову категорію."""
    new_category = Category(**data)
    db_session.add(new_category)
    db_session.commit()
    return CategorySchema(new_category).to_dict()

def get_all_categories():
    """Отримати список усіх категорій."""
    categories = db_session.query(Category).all()
    return [CategorySchema(category).to_dict() for category in categories]

def get_category_by_id(category_id):
    """Отримати категорію за її ID."""
    category = db_session.query(Category).filter(Category.id == category_id).first()
    return CategorySchema(category).to_dict() if category else None

def update_category(category_id, data):
    """Оновити дані категорії."""
    category = db_session.query(Category).filter(Category.id == category_id).first()
    if category:
        for key, value in data.items():
            setattr(category, key, value)
        db_session.commit()
        return CategorySchema(category).to_dict()
    return None

def delete_category(category_id):
    """Видалити категорію за її ID."""
    category = db_session.query(Category).filter(Category.id == category_id).first()
    if category:
        db_session.delete(category)
        db_session.commit()
        return CategorySchema(category).to_dict()
    return None
