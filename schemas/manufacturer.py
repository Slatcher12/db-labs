class ManufacturerSchema:
    """Схема для виробника."""

    def __init__(self, manufacturer):
        self.id = manufacturer.id
        self.name = manufacturer.name
        self.adress = manufacturer.adress
        self.contact_info = manufacturer.contact_info
        self.manufacturercol = manufacturer.manufacturercol
        self.medicine_id = manufacturer.medicine_id

    def to_dict(self):
        """Перетворити об'єкт у словник."""
        return {
            "id": self.id,
            "name": self.name,
            "adress": self.adress,
            "contact_info": self.contact_info,
            "manufacturercol": self.manufacturercol,
            "medicine_id": self.medicine_id
        }
