from pydantic import BaseModel, Field
from datetime import date
from decimal import Decimal

class FOMBAView(BaseModel):
    Declaration_ID: int
    Declarant_ID: str | None
    
    Date: date | None
    Office_ID: int | None
    office: str | None
    region: str | None
    Process_Type: str | None
    Import_Type: int | None
    Payment_Type: int | None
    Mode_of_Transport: int | None
    HS6_Code: str | None
    Country_of_Departure: str | None
    Country_of_Origin: str | None

    Net_Mass: Decimal | None
    Item_Price: Decimal | None

    Fraud: int | None
    Critical_Fraud: int | None

    cty_nam_fr: str | None
    importateur: str | None
    transporteur: str | None
    type_paiement: str | None
    regime: str | None

    class Config:
        from_attributes = True
