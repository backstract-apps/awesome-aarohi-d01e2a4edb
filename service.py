from sqlalchemy.orm import Session, aliased
from database import SessionLocal
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def delete_customers_customer_id(db: Session, customer_id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        customers_deleted = record_to_delete.to_dict()
    else:
        customers_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"customers_deleted": customers_deleted},
    }
    return res


async def get_customers(db: Session):

    query = db.query(models.Customers)

    customers_all = query.all()
    customers_all = (
        [new_data.to_dict() for new_data in customers_all]
        if customers_all
        else customers_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"customers_all": customers_all},
    }
    return res


async def get_customers_customer_id(db: Session, customer_id: int):

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))

    customers_one = query.first()

    customers_one = (
        (
            customers_one.to_dict()
            if hasattr(customers_one, "to_dict")
            else vars(customers_one)
        )
        if customers_one
        else customers_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"customers_one": customers_one},
    }
    return res


async def get_services(db: Session):

    query = db.query(models.Services)

    services_all = query.all()
    services_all = (
        [new_data.to_dict() for new_data in services_all]
        if services_all
        else services_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"services_all": services_all},
    }
    return res


async def post_customers(db: Session, raw_data: schemas.PostCustomers):
    name: str = raw_data.name
    contact_information: str = raw_data.contact_information

    record_to_be_added = {"name": name, "contact_information": contact_information}
    new_customers = models.Customers(**record_to_be_added)
    db.add(new_customers)
    db.commit()
    db.refresh(new_customers)
    customers_inserted_record = new_customers.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"customers_inserted_record": customers_inserted_record},
    }
    return res


async def put_customers_customer_id(
    db: Session, raw_data: schemas.PutCustomersCustomerId
):
    customer_id: int = raw_data.customer_id
    name: str = raw_data.name
    contact_information: str = raw_data.contact_information

    query = db.query(models.Customers)
    query = query.filter(and_(models.Customers.customer_id == customer_id))
    customers_edited_record = query.first()

    if customers_edited_record:
        for key, value in {
            "name": name,
            "customer_id": customer_id,
            "contact_information": contact_information,
        }.items():
            setattr(customers_edited_record, key, value)

        db.commit()
        db.refresh(customers_edited_record)

        customers_edited_record = (
            customers_edited_record.to_dict()
            if hasattr(customers_edited_record, "to_dict")
            else vars(customers_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"customers_edited_record": customers_edited_record},
    }
    return res


async def get_providers(db: Session):

    query = db.query(models.Providers)

    providers_all = query.all()
    providers_all = (
        [new_data.to_dict() for new_data in providers_all]
        if providers_all
        else providers_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"providers_all": providers_all},
    }
    return res


async def get_providers_provider_id(db: Session, provider_id: int):

    query = db.query(models.Providers)
    query = query.filter(and_(models.Providers.provider_id == provider_id))

    providers_one = query.first()

    providers_one = (
        (
            providers_one.to_dict()
            if hasattr(providers_one, "to_dict")
            else vars(providers_one)
        )
        if providers_one
        else providers_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"providers_one": providers_one},
    }
    return res


async def post_providers(db: Session, raw_data: schemas.PostProviders):
    name: str = raw_data.name
    specialization: str = raw_data.specialization

    record_to_be_added = {"name": name, "specialization": specialization}
    new_providers = models.Providers(**record_to_be_added)
    db.add(new_providers)
    db.commit()
    db.refresh(new_providers)
    providers_inserted_record = new_providers.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"providers_inserted_record": providers_inserted_record},
    }
    return res


async def put_providers_provider_id(
    db: Session, raw_data: schemas.PutProvidersProviderId
):
    provider_id: int = raw_data.provider_id
    name: str = raw_data.name
    specialization: str = raw_data.specialization

    query = db.query(models.Providers)
    query = query.filter(and_(models.Providers.provider_id == provider_id))
    providers_edited_record = query.first()

    if providers_edited_record:
        for key, value in {
            "name": name,
            "provider_id": provider_id,
            "specialization": specialization,
        }.items():
            setattr(providers_edited_record, key, value)

        db.commit()
        db.refresh(providers_edited_record)

        providers_edited_record = (
            providers_edited_record.to_dict()
            if hasattr(providers_edited_record, "to_dict")
            else vars(providers_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"providers_edited_record": providers_edited_record},
    }
    return res


async def delete_providers_provider_id(db: Session, provider_id: int):

    query = db.query(models.Providers)
    query = query.filter(and_(models.Providers.provider_id == provider_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        providers_deleted = record_to_delete.to_dict()
    else:
        providers_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"providers_deleted": providers_deleted},
    }
    return res


async def get_services_service_id(db: Session, service_id: int):

    query = db.query(models.Services)
    query = query.filter(and_(models.Services.service_id == service_id))

    services_one = query.first()

    services_one = (
        (
            services_one.to_dict()
            if hasattr(services_one, "to_dict")
            else vars(services_one)
        )
        if services_one
        else services_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"services_one": services_one},
    }
    return res


async def post_services(db: Session, raw_data: schemas.PostServices):
    name: str = raw_data.name
    duration_minutes: int = raw_data.duration_minutes

    record_to_be_added = {"name": name, "duration_minutes": duration_minutes}
    new_services = models.Services(**record_to_be_added)
    db.add(new_services)
    db.commit()
    db.refresh(new_services)
    services_inserted_record = new_services.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"services_inserted_record": services_inserted_record},
    }
    return res


async def put_services_service_id(db: Session, raw_data: schemas.PutServicesServiceId):
    service_id: int = raw_data.service_id
    name: str = raw_data.name
    duration_minutes: int = raw_data.duration_minutes

    query = db.query(models.Services)
    query = query.filter(and_(models.Services.service_id == service_id))
    services_edited_record = query.first()

    if services_edited_record:
        for key, value in {
            "name": name,
            "service_id": service_id,
            "duration_minutes": duration_minutes,
        }.items():
            setattr(services_edited_record, key, value)

        db.commit()
        db.refresh(services_edited_record)

        services_edited_record = (
            services_edited_record.to_dict()
            if hasattr(services_edited_record, "to_dict")
            else vars(services_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"services_edited_record": services_edited_record},
    }
    return res


async def delete_services_service_id(db: Session, service_id: int):

    query = db.query(models.Services)
    query = query.filter(and_(models.Services.service_id == service_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        services_deleted = record_to_delete.to_dict()
    else:
        services_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"services_deleted": services_deleted},
    }
    return res


async def get_appointments(db: Session):

    query = db.query(models.Appointments)

    appointments_all = query.all()
    appointments_all = (
        [new_data.to_dict() for new_data in appointments_all]
        if appointments_all
        else appointments_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"appointments_all": appointments_all},
    }
    return res


async def get_appointments_appointment_id(db: Session, appointment_id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.appointment_id == appointment_id))

    appointments_one = query.first()

    appointments_one = (
        (
            appointments_one.to_dict()
            if hasattr(appointments_one, "to_dict")
            else vars(appointments_one)
        )
        if appointments_one
        else appointments_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"appointments_one": appointments_one},
    }
    return res


async def post_appointments(db: Session, raw_data: schemas.PostAppointments):
    start_time: str = raw_data.start_time
    end_time: str = raw_data.end_time
    customer_id: int = raw_data.customer_id
    provider_id: int = raw_data.provider_id
    service_id: int = raw_data.service_id

    record_to_be_added = {
        "end_time": end_time,
        "service_id": service_id,
        "start_time": start_time,
        "customer_id": customer_id,
        "provider_id": provider_id,
    }
    new_appointments = models.Appointments(**record_to_be_added)
    db.add(new_appointments)
    db.commit()
    db.refresh(new_appointments)
    appointments_inserted_record = new_appointments.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"appointments_inserted_record": appointments_inserted_record},
    }
    return res


async def put_appointments_appointment_id(
    db: Session, raw_data: schemas.PutAppointmentsAppointmentId
):
    appointment_id: int = raw_data.appointment_id
    start_time: str = raw_data.start_time
    end_time: str = raw_data.end_time
    customer_id: int = raw_data.customer_id
    provider_id: int = raw_data.provider_id
    service_id: int = raw_data.service_id

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.appointment_id == appointment_id))
    appointments_edited_record = query.first()

    if appointments_edited_record:
        for key, value in {
            "end_time": end_time,
            "service_id": service_id,
            "start_time": start_time,
            "customer_id": customer_id,
            "provider_id": provider_id,
            "appointment_id": appointment_id,
        }.items():
            setattr(appointments_edited_record, key, value)

        db.commit()
        db.refresh(appointments_edited_record)

        appointments_edited_record = (
            appointments_edited_record.to_dict()
            if hasattr(appointments_edited_record, "to_dict")
            else vars(appointments_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"appointments_edited_record": appointments_edited_record},
    }
    return res


async def delete_appointments_appointment_id(db: Session, appointment_id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.appointment_id == appointment_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        appointments_deleted = record_to_delete.to_dict()
    else:
        appointments_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"appointments_deleted": appointments_deleted},
    }
    return res
