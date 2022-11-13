from typing import Optional
from pydantic import Field, BaseModel
from src.webapi.v1.users import req_res_users_models


class RiderCreateRequest(req_res_users_models.UserCreateRequest):
    phone_number: str = Field(example="+54911112225454")
    preferred_location_latitude: float = Field(example=-34.612580)
    preferred_location_longitude: float = Field(example=-58.408061)
    preferred_location_name: str = Field(example='Av. Paseo Colón 850')


class RiderResponse(req_res_users_models.UserResponse):
    phone_number: str = Field(example="+54111522223333")
    preferred_location_latitude: float = Field(example=-34.612580)
    preferred_location_longitude: float = Field(example=-58.408061)
    preferred_location_name: str = Field(example='Av. Paseo Colón 850')


class RiderUpdateRequest(BaseModel):
    first_name: Optional[str] = Field(example="f_name")
    last_name: Optional[str] = Field(example="l_name")
    phone_number: Optional[str] = Field(example="+54911112225454")
    preferred_location_latitude: Optional[float] = Field(example=-34.612580)
    preferred_location_longitude: Optional[float] = Field(example=-58.408061)
    preferred_location_name: Optional[str] = \
        Field(example='Av. Paseo Colón 850')
