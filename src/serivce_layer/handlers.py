from lib2to3.pgen2 import driver

from src.webapi.v1.qualy_drivers.req_res_qualy_driver import Driver_qualification_response
from src.webapi.v1.qualy_passenger.req_res_qualy_passenger import Passenger_qualification_response
from src.domain.commands import (
    AdminCreateCommand,
    AdminGetCommand,
    Command,
    DriverCreateCommand,
    DriverGetCommand,
    DriverUpdateCommand,
    RiderCreateCommand,
    RiderGetCommand,
    RiderUpdateCommand,
    UserCreateCommand,
    UserGetCommand,
    UserSearchCommand,
    DriverQualyCreateCommand,
    DriverQualyGetCommand,
    DriverQualyGetAverageCommand,
    PassengerQualyCreateCommand,
    PassengerQualyGetCommand,
    PassengerQualyGetAverageCommand
)
from src.domain.events import (
    UserCreatedEvent
)
from src.no_sql_database.no_sql_db import driver_collection,passenger_collection

from src.serivce_layer.abstract_unit_of_work import AbstractUnitOfWork

from src.domain.user import User
from src.domain.rider import Rider
from src.domain.driver import Driver
from src.domain.car import Car
from src.domain.location import Location
from src.domain.admin import Admin
from src.domain.driver_qualification import Driver_qualification


def _user_from_cmd(cmd: Command) -> User:
    return User(
        username=cmd.username,
        first_name=cmd.first_name,
        last_name=cmd.last_name,
        email=cmd.email,
        blocked=False,
        events=[]
    )


def _location_from_cmd(cmd: Command) -> Location:
    return Location(
        cmd.preferred_location_latitude,
        cmd.preferred_location_longitude,
        cmd.preferred_location_name
    )


def _car_from_cmd(cmd: Command) -> Car:
    return Car(
        plate=cmd.car_plate,
        manufacturer=cmd.car_manufacturer,
        model=cmd.car_model,
        year_of_production=cmd.car_year_of_production,
        color=cmd.car_color
        )


def _rider_from_cmd(cmd: Command) -> Rider:
    return Rider(
        username=cmd.username,
        first_name=cmd.first_name,
        last_name=cmd.last_name,
        email=cmd.email,
        blocked=False,
        events=[],
        phone_number=cmd.phone_number,
        wallet=cmd.wallet,
        location=_location_from_cmd(cmd)
    )


def _driver_from_cmd(cmd: Command) -> Driver:
    return Driver(
        username=cmd.username,
        first_name=cmd.first_name,
        last_name=cmd.last_name,
        email=cmd.email,
        blocked=False,
        events=[],
        phone_number=cmd.phone_number,
        wallet=cmd.wallet,
        location=_location_from_cmd(cmd),
        car=_car_from_cmd(cmd)
    )


def get_user(cmd: UserGetCommand, uow: AbstractUnitOfWork):
    with uow:
        user = uow.user_repository.find_by_email_or_username(
            username=cmd.username,
            email=cmd.username)
        uow.commit()
        return user


def search_user(cmd: UserSearchCommand, uow: AbstractUnitOfWork):
    with uow:
        user = uow.user_repository.search_by_username_like(
            like=cmd.username_like
        )
        uow.commit()
        return user


def create_user(cmd: UserCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user = _user_from_cmd(cmd)
        uow.user_repository.save(user)
        uow.commit()
        return user


def get_rider(cmd: RiderGetCommand, uow: AbstractUnitOfWork):
    with uow:
        rider = uow.rider_repository.find_by_email(cmd.email)
        uow.commit()
        return rider


def create_rider(cmd: RiderCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user = _user_from_cmd(cmd)
        uow.user_repository.save(user)
        rider = _rider_from_cmd(cmd)
        uow.rider_repository.save(rider)
        uow.commit()
        return rider


def update_rider(cmd: RiderUpdateCommand, uow: AbstractUnitOfWork):
    with uow:
        rider: Rider = uow.rider_repository.find_by_email(cmd.email)
        if cmd.first_name:
            rider.first_name = cmd.first_name
        if cmd.last_name:
            rider.last_name = cmd.last_name
        if cmd.phone_number:
            rider.phone_number = cmd.phone_number
        if cmd.wallet:
            rider.wallet = cmd.wallet
        loc_name = cmd.preferred_location_name
        loc_lat = cmd.preferred_location_latitude
        loc_long = cmd.preferred_location_longitude
        if loc_name and loc_lat and loc_long:
            rider.location = Location(loc_lat, loc_long, loc_name)
        updated_rider = uow.rider_repository.update(rider)
        uow.commit()
        return updated_rider


def create_driver(cmd: DriverCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        # FIXME: Fijarse que no exista, handlear bien
        user = _user_from_cmd(cmd)
        uow.user_repository.save(user)
        driver = _driver_from_cmd(cmd)
        uow.driver_repository.save(driver)
        uow.commit()
        return driver


def get_driver(cmd: DriverGetCommand, uow: AbstractUnitOfWork):
    with uow:
        driver = uow.driver_repository.find_by_email(cmd.email)
        uow.commit()
        return driver


def update_driver(cmd: DriverUpdateCommand, uow: AbstractUnitOfWork):
    with uow:
        driver: Driver = uow.driver_repository.find_by_email(cmd.email)
        if cmd.first_name:
            driver.first_name = cmd.first_name
        if cmd.last_name:
            driver.last_name = cmd.last_name
        if cmd.phone_number:
            driver.phone_number = cmd.phone_number
        if cmd.wallet:
            driver.wallet = cmd.wallet
        loc_name = cmd.preferred_location_name
        loc_lat = cmd.preferred_location_latitude
        loc_long = cmd.preferred_location_longitude
        if loc_name and loc_lat and loc_long:
            driver.location = Location(loc_lat, loc_long, loc_name)
        updated_driver = uow.driver_repository.update(driver)
        uow.commit()
        return updated_driver


def create_admin(cmd: AdminCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user: User = uow.user_repository.find_by_email(cmd.email)
        admin: Admin = Admin(username=user.username,
                             first_name=user.first_name,
                             last_name=user.last_name,
                             email=user.email,
                             blocked=False,
                             events=[])
        uow.admin_repository.save(admin)
        uow.commit()
        return admin


def get_admin(cmd: AdminGetCommand, uow: AbstractUnitOfWork):
    with uow:
        admin: Admin = uow.admin_repository.find_by_email(cmd.email)
        uow.commit()
        return admin


def publish_created_event(event: UserCreatedEvent,
                          uow: AbstractUnitOfWork):
    print(f'Created event {event}')







def command_to_dict(command_mongo):
    new_command = {"passenger_username": command_mongo.passenger_username,
    "qualy": command_mongo.qualy,
    "opinion": command_mongo.opinion,
    "driver_username": command_mongo.driver_username}
    return new_command

def bson_to_dict(item):
    print(item)
    if("opinion" in item):
        new_dict = {
            "passenger_username": item["passenger_username"],
            "qualy": item["qualy"],
            "opinion": item["opinion"],
            "driver_username": item["driver_username"]
        }
        return new_dict
    return None

def mongo_docs_to_list(doc):
    lista =[]
    for item in doc:
        new_item = bson_to_dict(item)
        if new_item != None:
            lista.append(new_item)
    return lista


def average_calculation(docs):
    cant_docs = 0
    suma = 0
    for item in docs:
        suma = suma + item["qualy"]
        cant_docs +=1
    promedio = suma // cant_docs
    return promedio

def get_qualy_driver(cmd: DriverQualyGetCommand, uow: AbstractUnitOfWork):
    docs = driver_collection.find({"driver_username":cmd.driver_username})
    lista_docs = mongo_docs_to_list(docs)
    return lista_docs
    

    
def create_qualy_driver(cmd: DriverQualyCreateCommand, uow: AbstractUnitOfWork):
    #pasa0r de cmd a objeto-crear-metodo
    cmd_as_dict = command_to_dict(cmd)
    id = driver_collection.insert_one(cmd_as_dict)
    return Driver_qualification_response(passenger_username=cmd.passenger_username,
    qualy  = cmd.qualy,
    opinion=cmd.opinion,
    driver_username = cmd.driver_username)


def get_qualy_average_driver(cmd: DriverQualyGetAverageCommand, uow: AbstractUnitOfWork):
    docs = driver_collection.find({"driver_username":cmd.driver_username})
    promedio = average_calculation(docs)
    return promedio
    


def get_qualy_passenger(cmd: PassengerQualyGetCommand, uow: AbstractUnitOfWork):
    docs = passenger_collection.find({"passenger_username":cmd.passenger_username})
    lista_docs = mongo_docs_to_list(docs)
    return lista_docs
    

    
def create_qualy_passenger(cmd: PassengerQualyCreateCommand, uow: AbstractUnitOfWork):
    #pasa0r de cmd a objeto-crear-metodo
    cmd_as_dict = command_to_dict(cmd)
    id = passenger_collection.insert_one(cmd_as_dict)
    return Passenger_qualification_response(passenger_username=cmd.passenger_username,
    qualy  = cmd.qualy,
    opinion=cmd.opinion,
    driver_username = cmd.driver_username)



def get_qualy_average_passenger(cmd: PassengerQualyGetAverageCommand, uow: AbstractUnitOfWork):
    docs = passenger_collection.find({"passenger_username":cmd.passenger_username})
    promedio = average_calculation(docs)
    return promedio