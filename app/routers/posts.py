from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get(path="", status_code=status.HTTP_200_OK)
async def get_posts() -> JSONResponse:
    return JSONResponse([{"id": 1, "title": "Post 1"}, {"id": 2, "title": "Post 2"}])
