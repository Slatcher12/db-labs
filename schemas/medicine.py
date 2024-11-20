class MedicineSchema:
    """Схема для лікарського засобу."""

    def __init__(self, medicine):
        self.id = medicine.id
        self.name = medicine.name
        self.description = medicine.description

    def to_dict(self):
        """Перетворити об'єкт у словник."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
