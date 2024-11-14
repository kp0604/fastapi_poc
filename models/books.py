from sqlalchemy import String,Integer,Boolean,Column,text,TIMESTAMP,ARRAY,ForeignKey
from ..connection import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession

class Books(Base):

    __tablename__ = 'books' 

    id = Column(Integer,primary_key = True , index = True)
    name =  Column(String, index= True)
    genre =  Column(String, index= True)
    sells = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author =  relationship("Authors", back_populates="books")
    

@classmethod
async def get_authors_if_books(db:AsyncSession):
        query = text("SELECT DISTINCT a.* FROM authors a INNER JOIN books b ON a.id = b.author_id")
        result = await db.execute(query)
        return result

@classmethod
async def get_books(db:AsyncSession):
        query = text("SELECT * FROM books")
        result = await db.execute(query)
        return result

@classmethod
async def get_books_of_author(db:AsyncSession,id:int):
        query = text("SELECT * FROM authors WHERE author_id = :id")
        result = await db.execute(query,{"id":id})
        return result


from pydantic import BaseModel
from typing import List

class BooksBase(BaseModel):
       name : str
       genre : int 
       sells : int
       

