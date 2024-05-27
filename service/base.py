from sqlalchemy import select, insert, delete, update

from database import async_session_maker


class BaseService:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.unique().scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.unique().scalars().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, object_id, **data):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == object_id).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, user_id, product_id):
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.user_id == user_id, cls.model.product_id == product_id)
            await session.execute(query)
            await session.commit()
