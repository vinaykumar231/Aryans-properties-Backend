from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from ..models.description import Description
from ..schemas import DescriptionCreate, DescriptionUpdate, DescriptionResponse
from sqlalchemy.exc import SQLAlchemyError
from ..models.property import Property

router = APIRouter()

@router.post("/description/", response_model=None)
def create_description(
    description: DescriptionCreate,
    db: Session = Depends(get_db)
):
    try:
        db_property = db.query(Property).filter(Property.property_code == description.property_id).first()
        if not db_property:
            raise HTTPException(status_code=404, detail="property id not found")
        
        count = db.query(Description).count() + 1
        des_id = f"D{count:03}"
        db_description = Description(
            des_id=des_id,
            description=description.description,
            property_id=description.property_id
        )
        db.add(db_description)
        db.commit()
        db.refresh(db_description)
        return db_description
    except HTTPException as http_exc:
        raise http_exc
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=404, detail="A database error occurred while adding description.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred while adding description.")

@router.get("/description/{des_id}", response_model=None)
def get_description(
    des_id: str,
    db: Session = Depends(get_db)
):
    try:
        db_description = db.query(Description).filter(Description.des_id == des_id).first()
        if not db_description:
            raise HTTPException(status_code=404, detail="Description not found")
        return db_description
    except HTTPException as http_exc:
        raise http_exc
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=404, detail="A database error occurred while fetching description.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching description.")

@router.get("/descriptions/", response_model=None)
def get_descriptions(db: Session = Depends(get_db)):
    try:
        descriptions = db.query(Description).all()
        if not descriptions:
            raise HTTPException(status_code=404, detail="No descriptions found")
        return descriptions
    except HTTPException as http_exc:
        raise http_exc
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=404, detail="A database error occurred while fetching descriptions.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching descriptions.")

@router.put("/description/{des_id}", response_model=None)
def update_description(
    des_id: str,
    description_update: DescriptionUpdate,
    db: Session = Depends(get_db)
):
    try:
        db_description = db.query(Description).filter(Description.des_id == des_id).first()
        if not db_description:
            raise HTTPException(status_code=404, detail="Description not found")
        
        db_description.description = description_update.description
        db_description.edit_date = datetime.utcnow()
        db.commit()
        db.refresh(db_description)
        return db_description
    except HTTPException as http_exc:
        raise http_exc
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=404, detail="A database error occurred while updating description.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred while updating description.")

@router.delete("/description/{des_id}", response_model=None)
def delete_description(
    des_id: str,
    db: Session = Depends(get_db)
):
    try:
        db_description = db.query(Description).filter(Description.des_id == des_id).first()
        if not db_description:
            raise HTTPException(status_code=404, detail="Description not found")
        
        db.delete(db_description)
        db.commit()
        return db_description
    except HTTPException as http_exc:
        raise http_exc
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=404, detail="A database error occurred while deleting description.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred while deleting description.")
