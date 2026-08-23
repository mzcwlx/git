from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI,HTTPException
import uvicorn
from fastapi import Path
from pydantic import BaseModel,Field
from fastapi.responses import HTMLResponse, JSONResponse,RedirectResponse
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from datetime import datetime
from sqlalchemy import Float, Integer, String, DateTime, func, select
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str




ASYNC_DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3306/FastAPI_database?charset=utf8"
async_engine = create_async_engine(
    ASYNC_DATABASE_URL, echo=True, pool_size=10, max_overflow=20
)

class Base(DeclarativeBase):
    create_time:Mapped[datetime]=mapped_column(DateTime,insert_default=func.now(),default=func.now(),comment="创建时间")
    update_time:Mapped[datetime]=mapped_column(DateTime,insert_default=func.now(),default=func.now(),onupdate=func.now(),comment="更新时间")

class Book(Base):
    __tablename__ = "book"
    id:Mapped[int]=mapped_column(primary_key=True,comment="书籍id")
    bookname:Mapped[str]=mapped_column(String(255),comment="书名")
    author:Mapped[str]=mapped_column(String(255),comment="作者")
    price:Mapped[float]=mapped_column(Float,comment="价格")
    publisher:Mapped[str]=mapped_column(String(255),comment="出版社")

async def creat_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def startup_event(app:FastAPI):
    await creat_tables()
    yield

app = FastAPI(lifespan=startup_event)

AsyncSessionLocal=async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_database():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

class BookBase(BaseModel):
    id:int
    bookname:str
    author:str
    price:float
    publisher:str
            
@app.get("/book/all")
async def get_book_list(db:AsyncSession = Depends(get_database)):
    result=await db.execute(select(Book))
    book=result.scalars().all()
    return book

@app.post("/book/add")
async def add_book(book:BookBase,db:AsyncSession = Depends(get_database)):
    book_obj=Book(**book.__dict__)
    db.add(book_obj)
    await db.commit()
    return book

@app.put("/book/updata")
async def updata_book(book:BookBase,book_id:int,db:AsyncSession = Depends(get_database)):
    db_book=await db.get(Book,book_id)
    if db_book is None:
        raise HTTPException(status_code=404,detail="书籍不存在")
    db_book.bookname=book.bookname
    db_book.author=book.author
    db_book.price=book.price
    db_book.publisher=book.publisher
    db_book.id=book.id
    await db.commit()
    return db_book,{"msg":"图书上传成功"}

@app.delete("/book/delete/{book_id}")
async def delete_book(book_id:int,db:AsyncSession = Depends(get_database)):
    db_book=await db.get(Book,book_id)
    if db_book is None:
        raise HTTPException(status_code=404,detail="书籍不存在")
    await db.delete(db_book)
    await db.commit()
    return {"msg":"删除图书成功"}


@app.get("/book/{book_id}")
async def get_book_list(book_id:int,db:AsyncSession = Depends(get_database)):
    result=await db.execute(select(Book).where(Book.id==book_id))
    book=result.scalar_one_or_none()
    return book


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)