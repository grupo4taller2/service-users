from fastapi import FastAPI, APIRouter
from typing import Optional
app = FastAPI(
    title="Users API", openapi_url="/openapi.json"
)


api_router = APIRouter()

USERS = [
    {
        'id': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
        'first_name': 'Mateo',
        'last_name': 'Calvo',
        'username': 'calvomateo'
    },
    {
        'id': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
        'first_name': 'Pedro',
        'last_name': 'Perez',
        'username': 'pedroperez'
    },
    {
        'id': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
        'first_name': 'Pablo',
        'last_name': 'Perez',
        'username': 'pabloperez'
    },
    {
        'id': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
        'first_name': 'Lucas',
        'last_name': 'Perez',
        'username': 'lucasperez'
    },
    {
        'id': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
        'first_name': 'Lionel',
        'last_name': 'Messi',
        'username': 'liomessi'
    },
    {
        'id': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
        'first_name': 'Lisa',
        'last_name': 'Su',
        'username': 'lisasu'
    }
]


@api_router.get("/users/{user_id}", status_code=200)
def fetch_user(user_id: str) -> dict:
    """
    Fetch a single user by ID
    """
    result = [u for u in USERS if u['id'] == user_id]
    if result:
        return result[0]


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}

@api_router.get('/search/', status_code=200)
def search_user(username: Optional[str] = None, max_results: Optional[int] = 2) -> dict:
    """
    Search for users based on username
    """
    if not username:
        return {'results': []}
    results = filter(lambda u: username.lower() in u['username'], USERS)
    return {'results': list(results)[:max_results]}


app.include_router(api_router)
