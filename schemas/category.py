class CategorySchema:
    """Схема для категорії."""

    def __init__(self, category):
        self.id = category.id
        self.name = category.name
        self.description = category.description
        self.medicine_id = category.medicine_id

    def to_dict(self):
        """Перетворити об'єкт у словник."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "medicine_id": self.medicine_id
        }
