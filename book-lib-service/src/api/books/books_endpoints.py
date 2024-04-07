from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from ..models.books_model import BooksCheckoutPayload, BookStatus, bookStatus, BooksReturnPayload
from ...db.mongo_utils import get_collection, get_client, get_database
books_router = APIRouter(prefix="/books", tags=[])

client = get_client()
db = get_database(client, "books_db")
issued_books_collection = get_collection(db, "issued_books_collection")
@books_router.post("/checkout/{book_id}", description="Checking out a book")
async def book_checkout(
    payload: BooksCheckoutPayload,
    issued_id: str
):
    try:
        payload = payload.dict()
        curr_date = datetime.utcnow()
        to_be_returned_date = curr_date + timedelta(days=payload["borrowing_days"])
        db_payload = BookStatus(
            issued_id=issued_id,
            book_id=payload["book_id"],
            book_status=bookStatus.CHECKOUT,
            date_issued=curr_date,
            borrower_name=payload["borrower_name"],
            issuer_name=payload["issuer_name"],
            date_to_be_returned=to_be_returned_date
        )
        issued_books_collection.insert_one(db_payload)
        return JSONResponse(
            status_code= 200,
            content="Book has been issued"
        )
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error checking out the book:: {repr(e)}"
        ) from e
        
@books_router.post("/returned/{book_id}", description="returning out a book")
async def book_checkout(
    payload: BooksReturnPayload 
):
    try:
        issued_id = payload["issued_id"]
        """
        get book status(this is a query which was to be implemented) from the collection of issued book and then check the extra days for fine,
        then add the new date for where we update the submission of the book and reponse with 200 along with any fine received, 
        due to lack of time cant implement it
        
        """
        # get_book_status = await book_status(issued_id)
        return JSONResponse(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            content="not implemented"
        )
    except Exception as e:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error checking out the book:: {repr(e)}"
        ) from e