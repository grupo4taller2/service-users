from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any

from src.crud.crud_user import user

from src.api import deps
from src.schemas.user import User

router = APIRouter()


@router.get("/{username}", status_code=200, response_model=User)
def fetch_user(username: str,
               db: Session = Depends(deps.get_db)) -> Any:
    """
    Fetch a single user by username
    """

    result = user.get_by_username(db=db, username=username)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {username} not found"
        )
    print(result)
    return result
