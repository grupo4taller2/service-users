from fastapi import FastAPI, APIRouter
from src.core.config import settings
from src.api.api_v1.api import api_router

root_router = APIRouter()
app = FastAPI(title="Users API", openapi_url="/openapi.json")
app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

'''
@api_router.get("/users/{username}", status_code=200, response_model=User)
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


@api_router.get("/", status_code=200, response_model=UserSearchResult)
def root(request: Request,
         db: Session = Depends(deps.get_db)) -> dict:
    """
    Root Get
    """
    users = user.get_multi(db=db, limit=10)
    return {"results": list(users)}


@api_router.get('/search/', status_code=200, response_model=UserSearchResult)
def search_user(username: Optional[str] = Query(None,
                                                min_lenght=3,
                                                example='liomessi'),
                max_results: Optional[int] = 2,
                db: Session = Depends(deps.get_db)) -> dict:
    """
    Search for users based on username
    """
    if not username:
        return {'results': []}
    users = user.get_multi(db=db, limit=max_results)
    results = filter(lambda u: username.lower() in u.username.lower(), users)
    return {'results': list(results)}


@api_router.post("/users/", status_code=201, response_model=User)
def create_ruser(user_in: User) -> User:
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
'''
