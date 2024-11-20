from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Конфігурація підключення до бази даних
DATABASE_URL = "mysql+pymysql://root:password@localhost/mydb"

# Створення двигуна бази даних
engine = create_engine(DATABASE_URL, echo=True)

# Налаштування сесії
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Базовий клас для моделей
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """Ініціалізація бази даних."""
    import models.category
    import models.manufacturer
    import models.medicine
    Base.metadata.create_all(bind=engine)
