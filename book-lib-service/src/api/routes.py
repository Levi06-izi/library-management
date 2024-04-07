from fastapi import APIRouter

from .books import books_endpoints

router = APIRouter()

router.include_router(books_endpoints.books_router, prefix="", dependencies=[])