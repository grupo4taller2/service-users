from pydantic import Field
from src.entrypoints.http.api.v1 import req_res_users_models


class RiderCreateRequest(req_res_users_models.UserCreateRequest):
    phone_number: str = Field(example="+54911112225454")
    wallet: str = Field(example="sh4kf84ert544uo")
    preferred_location_latitude: float = Field(example=-34.612580)
    preferred_location_longitude: float = Field(example=-58.408061)
    preferred_location_name: str = Field(example='Av. Paseo Colón 850')


class RiderResponse(req_res_users_models.UserResponse):
    phone_number: str = Field(example="cryptowallet")
    wallet: str = Field(example="cryptowallet")
    preferred_location_latitude: float = Field(example=-34.612580)
    preferred_location_longitude: float = Field(example=-58.408061)
    preferred_location_name: str = Field(example='Av. Paseo Colón 850')
