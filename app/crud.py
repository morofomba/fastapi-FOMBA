from sqlalchemy.orm import Session
from . import models, schemas
from .models import FOMBA
from sqlalchemy import func
from fastapi import APIRouter
#def get_all_FOMBA(db: Session):
 #   return db.query(FOMBA).all()
router = APIRouter()

@router.get("/items")
def get_items():
    return {"items": []}

def get_all_FOMBA(db: Session, limit: int = 50):
    return (
        db.query(FOMBA)
        .limit(limit)
        .all()
    )


def get_fomba_by_bureau(db: Session, office_id: int):
    return (
        db.query(FOMBA)
        .filter(FOMBA.Office_ID == office_id)
        .all()
    )

def get_fomba_by_pays(db: Session, nom_pays: str):
    return (
        db.query(FOMBA)
        .filter(
            func.unaccent(func.lower(FOMBA.cty_nam_fr)) ==
            func.unaccent(func.lower(nom_pays))
        )
        .all()
    )

def get_fomba_by_importateur(db, nom_importateur: str):
    return (
        db.query(FOMBA)
        .filter(
            func.lower(FOMBA.importateur) == nom_importateur.lower()
        )
        .all()
    )


def get_fomba_by_declarant_id(db: Session, declarant_id: str):
    return (
        db.query(FOMBA)
        .filter(FOMBA.Declarant_ID == declarant_id)
        .all()
    )




def get_fomba_by_regime(db, regime: str):
    return (
        db.query(FOMBA)
        .filter(
            func.unaccent(func.lower(FOMBA.regime)) ==
            func.unaccent(func.lower(regime))
        )
        .all()
    )