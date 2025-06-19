from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models.database import engine
from models.schemas import Customer

router = APIRouter()

@router.post("/customers/")
def create_customer(customer: Customer):
    with Session(engine) as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer

@router.get("/customers/")
def get_customers():
    with Session(engine) as session:
        return session.exec(select(Customer)).all()

@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, updated: Customer):
    with Session(engine) as session:
        db_customer = session.get(Customer, customer_id)
        if not db_customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        for key, value in updated.dict(exclude_unset=True).items():
            setattr(db_customer, key, value)
        session.commit()
        return db_customer

@router.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    with Session(engine) as session:
        customer = session.get(Customer, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        session.delete(customer)
        session.commit()
        return {"message": "Customer deleted"}