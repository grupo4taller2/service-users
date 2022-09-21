from fastapi import FastAPI, APIRouter, Query, HTTPException
from fastapi.responses import JSONResponse

from typing import Optional, Any

from src.schemas.user import User
from src.schemas.user_search_result import UserSearchResult

app = FastAPI(
    title="Users API", openapi_url="/openapi.json"
)

api_router = APIRouter()

USERS = [
    {
        'first_name': 'Mateo',
        'last_name': 'Calvo',
        'username': 'calvomateo',
        'email': 'mateo@mateo.com'
    },
    {
        'first_name': 'Pedro',
        'last_name': 'Perez',
        'username': 'pedroperez',
        'email': 'pedro@perez.com'
    },
    {
        'first_name': 'Pablo',
        'last_name': 'Perez',
        'username': 'pabloperez',
        'email': 'pablo@perez.com'
    },
    {
        'first_name': 'Lucas',
        'last_name': 'Perez',
        'username': 'lucasperez',
        'email': 'lucas@perez.com'
    },
    {
        'first_name': 'Lionel',
        'last_name': 'Messi',
        'username': 'liomessi',
        'email': 'lio@messi.com'
    },
    {
        'first_name': 'Lisa',
        'last_name': 'Su',
        'username': 'lisasu',
        'email': 'lisasu@amd.com'
    }
]


@api_router.get("/users/{username}", status_code=200, response_model=User)
def fetch_user(username: str) -> Any:
    """
    Fetch a single user by username
    """
    result = [u for u in USERS if u['username'] == username]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"User {username} not found"
        )
    return result[0]


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


@api_router.get('/search/', status_code=200, response_model=UserSearchResult)
def search_user(username: Optional[str] = Query(None, min_lenght=3, example='liomessi'), max_results: Optional[int] = 2) -> dict:
    """
    Search for users based on username
    """
    if not username:
        return {'results': []}
    results = filter(lambda u: username.lower() in u['username'], USERS)
    return {'results': list(results)[:max_results]}


@api_router.post("/users/", status_code=201, response_model=User)
def create_recipe(user_in: User) -> User:
    """
    Create a new user
    """
    user_entry: User = User(
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        username=user_in.username,
        email=user_in.email
    )
    USERS.append(user_entry.dict())
    return user_entry


app.include_router(api_router)
