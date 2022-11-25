from pydantic import Field, BaseModel


# TODO: Refactor name

class Push_token_creation(BaseModel):
    username: str = Field(example="cool_username")
    token: str = Field(example="asdadgghfgdsdwefdsdaNSA")

