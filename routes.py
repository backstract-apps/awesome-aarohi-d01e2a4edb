from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.delete('/customers/customer_id')
async def delete_customers_customer_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_customers_customer_id(db, customer_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/')
async def get_customers(db: Session = Depends(get_db)):
    try:
        return await service.get_customers(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/customers/customer_id')
async def get_customers_customer_id(customer_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_customers_customer_id(db, customer_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/services/')
async def get_services(db: Session = Depends(get_db)):
    try:
        return await service.get_services(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/customers/')
async def post_customers(raw_data: schemas.PostCustomers, db: Session = Depends(get_db)):
    try:
        return await service.post_customers(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/customers/customer_id/')
async def put_customers_customer_id(raw_data: schemas.PutCustomersCustomerId, db: Session = Depends(get_db)):
    try:
        return await service.put_customers_customer_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/providers/')
async def get_providers(db: Session = Depends(get_db)):
    try:
        return await service.get_providers(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/providers/provider_id')
async def get_providers_provider_id(provider_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_providers_provider_id(db, provider_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/providers/')
async def post_providers(raw_data: schemas.PostProviders, db: Session = Depends(get_db)):
    try:
        return await service.post_providers(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/providers/provider_id/')
async def put_providers_provider_id(raw_data: schemas.PutProvidersProviderId, db: Session = Depends(get_db)):
    try:
        return await service.put_providers_provider_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/providers/provider_id')
async def delete_providers_provider_id(provider_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_providers_provider_id(db, provider_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/services/service_id')
async def get_services_service_id(service_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_services_service_id(db, service_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/services/')
async def post_services(raw_data: schemas.PostServices, db: Session = Depends(get_db)):
    try:
        return await service.post_services(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/services/service_id/')
async def put_services_service_id(raw_data: schemas.PutServicesServiceId, db: Session = Depends(get_db)):
    try:
        return await service.put_services_service_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/services/service_id')
async def delete_services_service_id(service_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_services_service_id(db, service_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/')
async def get_appointments(db: Session = Depends(get_db)):
    try:
        return await service.get_appointments(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/appointment_id')
async def get_appointments_appointment_id(appointment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_appointments_appointment_id(db, appointment_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/appointments/')
async def post_appointments(raw_data: schemas.PostAppointments, db: Session = Depends(get_db)):
    try:
        return await service.post_appointments(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/appointments/appointment_id/')
async def put_appointments_appointment_id(raw_data: schemas.PutAppointmentsAppointmentId, db: Session = Depends(get_db)):
    try:
        return await service.put_appointments_appointment_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/appointments/appointment_id')
async def delete_appointments_appointment_id(appointment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_appointments_appointment_id(db, appointment_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

