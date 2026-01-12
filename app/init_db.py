from .database import Base, engine
from .models import FOMBA
Base.metadata.create_all(bind=engine)