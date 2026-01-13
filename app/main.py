from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import get_db
from pydantic import BaseModel
from datetime import date
from app.crud import router as crud_router
from app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def root():
    return {"message": "API FOMBA en ligne"}

app.include_router(crud_router, prefix="/api", tags=["CRUD"])

@app.get("/")
def read():
    return {"message": "Bienvenue dans ma Base 'FOMBA' "}

@app.get("/fomba", response_model=list[schemas.FOMBAView])
def get_fomba(db: Session = Depends(get_db)):
    return crud.get_all_FOMBA(db)

@app.get("/fomba/pays/{nom_pays}", response_model=list[schemas.FOMBAView])
def read_fomba_by_pays(nom_pays: str, db: Session = Depends(get_db)):
    return crud.get_fomba_by_pays(db, nom_pays)


@app.get("/fomba/bureau/{bureau}", response_model=list[schemas.FOMBAView])
def get_fomba_by_bureau(
    bureau: int,
    db: Session = Depends(get_db)
):
    return crud.get_fomba_by_bureau(db, bureau)

@app.get("/fomba/importateur/{nom_importateur}")
def read_fomba_by_importateur(
    nom_importateur: str,
    db: Session = Depends(get_db)
):
    return crud.get_fomba_by_importateur(db, nom_importateur)

@app.get("/fomba/declarant-id/{declarant_id}")
def read_by_declarant_id(
    declarant_id: str,
    db: Session = Depends(get_db)
):
    return crud.get_fomba_by_declarant_id(db, declarant_id)

@app.get("/fomba/regime/{regime}", response_model=list[schemas.FOMBAView])
def get_fomba_by_regime(regime: str, db: Session = Depends(get_db)):
    data = crud.get_fomba_by_regime(db, regime)
    if not data:
        raise HTTPException(status_code=404, detail="Régime non trouvé")
    return data


# ===== VIEW FOMBA =====
class FOMBAView(BaseModel):
    Declaration_ID: int
    Declarant_ID: str | None
    Date: date | None = None
    Office_ID: int | None = None
    Process_Type: str | None = None
    Country_of_Departure: str | None = None

    class Config:
        from_attributes = True


# ===== IMPORTATION =====
class ImportationSchema(BaseModel):
    Declaration_ID: int
    Country_of_Departure: str | None = None
    Import_Type: str | None = None
    HS6_Code: str | None = None
    Date: date | None = None

    class Config:
        from_attributes = True


# ===== BUREAU =====
class BureauSchema(BaseModel):
    Declaration_ID: int
    Office_ID: int | None = None

    class Config:
        from_attributes = True
