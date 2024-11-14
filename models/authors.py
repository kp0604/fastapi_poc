from sqlalchemy import String,Integer,Boolean,Column,text,TIMESTAMP,ARRAY,ForeignKey
from ..connection import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import List


# table
class Authors(Base):

    __tablename__ = 'authors' 

    id = Column(Integer,primary_key = True , index = True, autoincrement = True)
    name =  Column(String, index= True)
    genres =  Column(ARRAY(String), index= True)
    books = relationship("Books", back_populates="authors")

# schemas
class AuthorsBase(BaseModel):
       name : str
       genres : List[str]


# functions and procedures
@classmethod
async def get_authors(db:AsyncSession):
        query = text("SELECT * FROM authors")
        result = await db.execute(query)
        return result

@classmethod
async def get_authors_if_books(db:AsyncSession):
        query = text("SELECT DISTINCT a.* FROM authors a INNER JOIN books b ON a.id = b.author_id")
        result = await db.execute(query)
        return result

@classmethod
async def get_all_authors_books(db:AsyncSession):
        query = text("SELECT a.*,b.* FROM authors a FULL JOIN books b ON a.id = b.author_id")
        result = await db.execute(query)
        return result

@classmethod
async def get_all_authors_books1(db:AsyncSession):
        query = text("SELECT * FROM authors a FULL JOIN books b ON a.id = b.author_id")
        result = await db.execute(query)
        return result

@classmethod
async def add_author(db:AsyncSession,data:AuthorsBase):
        query = text("INSERT INTO authors VALUES(:name,:genres) RETURNING(id,name,genres)")
        result = await db.execute(query,{"name":data.name,"genres":data.genres})
        inserted = result.fetchone()
        await db.commit()
        return {"status":"added succesfully","data":inserted}