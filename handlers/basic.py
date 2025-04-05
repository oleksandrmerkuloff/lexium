from typing import Optional, Union, Type

from sqlalchemy import select
from sqlalchemy.orm import Session, DeclarativeMeta
from sqlalchemy.exc import NoResultFound, SQLAlchemyError


class BaseHandler:
    def __init__(self, db: Session, model: Type[DeclarativeMeta]) -> None:
        self.db = db
        self.model = model

    def add_record(self, data: dict) -> bool:
        try:
            new_record = self.model(**data)
            self.db.add(new_record)
        except SQLAlchemyError:
            self.db.rollback()
            return False
        self.db.commit()
        return True

    def edit_record(self, data: dict) -> bool:
        try:
            record = self.get_single_record("id", data["id"])
            if not record:
                raise NoResultFound("Record doesn't exsists!")
            for key, value in data.items():
                if key != "id" and hasattr(record, key):
                    setattr(record, key, value)
        except SQLAlchemyError:
            self.db.rollback()
            return False
        self.db.commit()
        return True

    def delete_record(
        self,
        search_column: str,
        search_key: Union[int, str]
    ) -> bool:
        try:
            to_delete_record = self.get_single_record(
                search_column, search_key
            )
            if not to_delete_record:
                raise NoResultFound("Record doesn't exsists!")
            self.db.delete(to_delete_record)
        except SQLAlchemyError:
            self.db.rollback()
            return False
        self.db.commit()
        return True

    def get_single_record(
        self,
        search_column: str,
        search_key: Union[int, str]
    ) -> Optional[DeclarativeMeta]:
        if not hasattr(self.model, search_column):
            raise ValueError("Wrong search key!")
        record = select(self.model).where(
            getattr(self.model, search_column) == search_key
            )
        result = self.db.execute(record).scalars().first()
        return result
