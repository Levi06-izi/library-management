from fastapi import APIRouter, HTTPException, status

member_router = APIRouter(prefix="/books", tags=[])
@member_router.get("/")
async def get_memebers():
    try:
        pass
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error checking out the book:: {repr(e)}"
        ) from e