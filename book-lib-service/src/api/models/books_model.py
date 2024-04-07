from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from pymongo import IndexModel

class BooksCheckoutPayload(BaseModel):
    """
    payloaad for checkout of a book
    """
    book_id: str
    book_name: str
    borrower_name: str
    borrowing_days: int
    issuer_name:str
    
class BooksReturnPayload(BaseModel):
    """
    payloaad for checkout of a book
    """
    issued_id: str
    book_id: str
    book_name: str
    librarian: str
    returnee_name: str
    date_returned: datetime
    

class bookStatus(str, Enum):
    """
    """
    CHECKOUT= "checkout"
    RETURNED="returned"
 
class BookStatus(BaseModel):
    """
    status model for book checkout-return cycle
    """
    issued_id: str
    book_id: str
    book_status: bookStatus
    date_issued: datetime
    borrower_name: str
    issuer_name: str
    date_to_be_returned: datetime
    date_returned: Optional[datetime] = None
    
    @staticmethod
    def generate_index_models() -> List[IndexModel]:
        return [
            IndexModel("issued_id"),
            IndexModel("book_id"),
            IndexModel("book_status")
        ]    
    
    