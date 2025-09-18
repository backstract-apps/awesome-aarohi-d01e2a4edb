from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Customers(BaseModel):
    name: Optional[str]=None
    contact_information: Optional[str]=None


class ReadCustomers(BaseModel):
    name: Optional[str]=None
    contact_information: Optional[str]=None
    class Config:
        from_attributes = True


class Providers(BaseModel):
    name: Optional[str]=None
    specialization: Optional[str]=None


class ReadProviders(BaseModel):
    name: Optional[str]=None
    specialization: Optional[str]=None
    class Config:
        from_attributes = True


class Services(BaseModel):
    name: Optional[str]=None
    duration_minutes: Optional[int]=None


class ReadServices(BaseModel):
    name: Optional[str]=None
    duration_minutes: Optional[int]=None
    class Config:
        from_attributes = True


class Appointments(BaseModel):
    start_time: Optional[Any]=None
    end_time: Optional[Any]=None
    customer_id: Optional[int]=None
    provider_id: Optional[int]=None
    service_id: Optional[int]=None


class ReadAppointments(BaseModel):
    start_time: Optional[Any]=None
    end_time: Optional[Any]=None
    customer_id: Optional[int]=None
    provider_id: Optional[int]=None
    service_id: Optional[int]=None
    class Config:
        from_attributes = True




class PostCustomers(BaseModel):
    name: Optional[str]=None
    contact_information: Optional[str]=None

    class Config:
        from_attributes = True



class PutCustomersCustomerId(BaseModel):
    customer_id: Optional[int]=None
    name: Optional[str]=None
    contact_information: Optional[str]=None

    class Config:
        from_attributes = True



class PostProviders(BaseModel):
    name: Optional[str]=None
    specialization: Optional[str]=None

    class Config:
        from_attributes = True



class PutProvidersProviderId(BaseModel):
    provider_id: Optional[int]=None
    name: Optional[str]=None
    specialization: Optional[str]=None

    class Config:
        from_attributes = True



class PostServices(BaseModel):
    name: Optional[str]=None
    duration_minutes: Optional[int]=None

    class Config:
        from_attributes = True



class PutServicesServiceId(BaseModel):
    service_id: Optional[int]=None
    name: Optional[str]=None
    duration_minutes: Optional[int]=None

    class Config:
        from_attributes = True



class PostAppointments(BaseModel):
    start_time: Optional[str]=None
    end_time: Optional[str]=None
    customer_id: Optional[int]=None
    provider_id: Optional[int]=None
    service_id: Optional[int]=None

    class Config:
        from_attributes = True



class PutAppointmentsAppointmentId(BaseModel):
    appointment_id: Optional[int]=None
    start_time: Optional[str]=None
    end_time: Optional[str]=None
    customer_id: Optional[int]=None
    provider_id: Optional[int]=None
    service_id: Optional[int]=None

    class Config:
        from_attributes = True

