from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean
from .database import Base

class FOMBA(Base):
    __tablename__ = "FOMBA"
    __table_args__ = {"schema": "HR"}

    Declaration_ID = Column(Integer, primary_key=True)

    # Colonnes de la VIEW
    Declaration_ID = Column("Declaration_ID", Integer, primary_key=True)
    Date = Column("Date", Date)
    Office_ID = Column("Office_ID", Integer)
    Process_Type = Column("Process_Type", String)
    Import_Type = Column("Import_Type", String)
    Payment_Type = Column("Payment_Type", String)
    Mode_of_Transport = Column("Mode_of_Transport", String)

    Declarant_ID = Column("Declarant_ID", Integer)
    Seller_ID = Column("Seller_ID", Integer)
    Courier_ID = Column("Courier_ID", Integer)

    HS6_Code = Column("HS6_Code", String)
    Country_of_Departure = Column("Country_of_Departure", String)
    Country_of_Origin = Column("Country_of_Origin", String)

    Tax_Rate = Column("Tax_Rate", Numeric)
    Tax_Type = Column("Tax_Type", String)
    Country_of_Origin_Indicator = Column("Country_of_Origin_Indicator", String)

    Net_Mass = Column("Net_Mass", Numeric)
    Item_Price = Column("Item_Price", Numeric)

    Fraud = Column("Fraud", Boolean)
    Critical_Fraud = Column("Critical_Fraud", Boolean)

    # Colonnes jointes
    cty_nam_fr = Column("CTY_NAM_FR", String)
    office = Column("OFFICE", String)
    region = Column("REGION", String)
    importateur = Column("Importateur", String)
    transporteur = Column("Transporteur", String)
    type_paiement = Column("TYPE_PAIEMENT", String)
    regime = Column("REGIME", String)
