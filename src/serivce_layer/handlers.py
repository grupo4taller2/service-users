# flake8: noqa

from src.webapi.v1.qualy_drivers.req_res_qualy_driver import (
    Driver_qualification_response,
)
from src.webapi.v1.qualy_rider.req_res_qualy_rider import (
    Rider_qualification_response,
)
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
    RiderQualyCreateCommand,
    RiderQualyGetCommand,
    RiderQualyGetAverageCommand,
    UserGetAllCommand,
    PushTokenCreateCommand,
    DriverGetAllCommand
)
from src.domain.events import (
    UserCreatedEvent
)
from src.no_sql_database.no_sql_db import driver_collection, \
                                        rider_collection, \
                                        token_collection

from src.serivce_layer.abstract_unit_of_work import AbstractUnitOfWork

from src.domain.user import User
from src.domain.rider import Rider
from src.domain.driver import Driver
from src.domain.car import Car
from src.domain.location import Location
from src.domain.admin import Admin

from fastapi import status
from fastapi.responses import JSONResponse


def _user_from_cmd(cmd: Command) -> User:
    return User(
        username=cmd.username,
        first_name=cmd.first_name,
        last_name=cmd.last_name,
        email=cmd.email,
        blocked=False,
        events=[],
    )


def _location_from_cmd(cmd: Command) -> Location:
    return Location(
        cmd.preferred_location_latitude,
        cmd.preferred_location_longitude,
        cmd.preferred_location_name,
    )


def _car_from_cmd(cmd: Command) -> Car:
    return Car(
        plate=cmd.car_plate,
        manufacturer=cmd.car_manufacturer,
        model=cmd.car_model,
        year_of_production=cmd.car_year_of_production,
        color=cmd.car_color,
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
        location=_location_from_cmd(cmd),
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
        location=_location_from_cmd(cmd),
        car=_car_from_cmd(cmd),
    )


def get_user(cmd: UserGetCommand, uow: AbstractUnitOfWork):
    with uow:
        user = uow.user_repository.find_by_email_or_username(
            username=cmd.username, email=cmd.username
        )
        uow.commit()
        return user


def get_all_users(cmd: UserGetAllCommand, uow: AbstractUnitOfWork):
    with uow:
        users = uow.user_repository.all(cmd.username_like,
                                        cmd.offset,
                                        cmd.limit)
        uow.commit()
        return users


def search_user(cmd: UserSearchCommand, uow: AbstractUnitOfWork):
    with uow:
        users = uow.user_repository.search_by_username_like(
            like=cmd.username_like
        )
        uow.commit()
        return users


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
        # user = _user_from_cmd(cmd)
        # uow.user_repository.save(user)
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
        # user = _user_from_cmd(cmd)
        # uow.user_repository.save(user)
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
        loc_name = cmd.preferred_location_name
        loc_lat = cmd.preferred_location_latitude
        loc_long = cmd.preferred_location_longitude
        if loc_name and loc_lat and loc_long:
            driver.location = Location(loc_lat, loc_long, loc_name)
        if cmd.car_manufacturer:
            driver.car.manufacturer = cmd.car_manufacturer
        if cmd.car_model:
            driver.car.model = cmd.car_model
        if cmd.car_year_of_production:
            driver.car.year_of_production = cmd.car_year_of_production
        if cmd.car_color:
            driver.car.color = cmd.car_color
        if cmd.car_plate:
            driver.car.plate = cmd.car_plate
        
        updated_driver = uow.driver_repository.update(driver)
        uow.commit()
        return updated_driver


def create_admin(cmd: AdminCreateCommand, uow: AbstractUnitOfWork):
    with uow:
        user: User = uow.user_repository.find_by_email(cmd.email)
        admin: Admin = Admin(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            blocked=False,
            events=[],
        )
        uow.admin_repository.save(admin)
        uow.commit()
        return admin


def get_admin(cmd: AdminGetCommand, uow: AbstractUnitOfWork):
    with uow:
        admin: Admin = uow.admin_repository.find_by_email(cmd.email)
        uow.commit()
        return admin


def publish_created_event(event: UserCreatedEvent, uow: AbstractUnitOfWork):
    print(f"Created event {event}")


def command_to_dict(command_mongo):
    new_command = {
        "rider_username": command_mongo.rider_username,
        "qualy": command_mongo.qualy,
        "opinion": command_mongo.opinion,
        "driver_username": command_mongo.driver_username,
    }
    return new_command


def bson_to_dict(item):
    print(item)
    if "opinion" in item:
        new_dict = {
            "rider_username": item["rider_username"],
            "qualy": item["qualy"],
            "opinion": item["opinion"],
            "driver_username": item["driver_username"],
        }
        return new_dict
    return None


def mongo_docs_to_list(doc):
    lista = []
    for item in doc:
        new_item = bson_to_dict(item)
        if new_item is not None:
            lista.append(new_item)
    return lista


def average_calculation(docs):
    cant_docs = 0
    suma = 0
    for item in docs:
        suma = suma + item["qualy"]
        cant_docs += 1
    if (cant_docs == 0):
        return 0
    promedio = round(suma / cant_docs, 1)
    return promedio


def get_qualy_driver(cmd: DriverQualyGetCommand, uow: AbstractUnitOfWork):
    if (driver_collection.count_documents(
            {"driver_username": cmd.driver_username}, limit = 1) == 0):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=str("Driver not found")
        )
    docs = driver_collection.find({"driver_username": cmd.driver_username})
    lista_docs = mongo_docs_to_list(docs)
    return lista_docs


def create_qualy_driver(cmd: DriverQualyCreateCommand,
                        uow: AbstractUnitOfWork):
    # pasa0r de cmd a objeto-crear-metodo
    cmd_as_dict = command_to_dict(cmd)
    driver_collection.insert_one(cmd_as_dict)
    return Driver_qualification_response(
        rider_username=cmd.rider_username,
        qualy=cmd.qualy,
        opinion=cmd.opinion,
        driver_username=cmd.driver_username,
    )


def get_qualy_average_driver(
    cmd: DriverQualyGetAverageCommand, uow: AbstractUnitOfWork
):
    if (driver_collection.count_documents({"driver_username": cmd.driver_username}, limit = 1) == 0):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=str("Driver not found")
    )
    docs = driver_collection.find({"driver_username": cmd.driver_username})
    promedio = average_calculation(docs)
    
    return promedio


def get_qualy_rider(cmd: RiderQualyGetCommand,
                    uow: AbstractUnitOfWork):
    if (rider_collection.count_documents({"rider_username": cmd.rider_username}, limit = 1) == 0):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=str("Rider not found")
        )
    docs = rider_collection \
            .find({"rider_username": cmd.rider_username})
    lista_docs = mongo_docs_to_list(docs)
    return lista_docs


def create_qualy_rider(cmd: RiderQualyCreateCommand,
                       uow: AbstractUnitOfWork):
    # pasa0r de cmd a objeto-crear-metodo
    cmd_as_dict = command_to_dict(cmd)
    rider_collection.insert_one(cmd_as_dict)
    return Rider_qualification_response(
        rider_username=cmd.rider_username,
        qualy=cmd.qualy,
        opinion=cmd.opinion,
        driver_username=cmd.driver_username,
    )


def get_qualy_average_rider(
    cmd: RiderQualyGetAverageCommand, uow: AbstractUnitOfWork
):
    if (rider_collection.count_documents({"rider_username": cmd.rider_username}, limit = 1) == 0):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content=str("Rider not found")
        )
    docs = rider_collection \
            .find({"rider_username": cmd.rider_username})
    
    promedio = average_calculation(docs)
    return promedio


def create_push_token(cmd: PushTokenCreateCommand,
                       uow: AbstractUnitOfWork):
    # pasa0r de cmd a objeto-crear-metodo
    if (token_collection.count_documents({"username": cmd.username}, limit = 1) == 0):
        token_collection.insert_one({
            "username": cmd.username,
            "token": cmd.token
        })
        return {
            "username": cmd.username,
            "token": cmd.token
            }
    else:
        filter = { "username": cmd.username }
        newvalues = { "$set": { "token": cmd.token } }
        token_collection.update_one(filter, newvalues)
        return {
            "username": cmd.username,
            "token": cmd.token
            }
    
def get_all_drivers(cmd:DriverGetAllCommand, uow: AbstractUnitOfWork):
    with uow:
        driver_list = uow.driver_repository.get_all_drivers_usernames()
        uow.commit()
        return driver_list