from typing import Optional, Union

from sqlalchemy import select
from sqlalchemy.orm import Session, DeclarativeMeta


class BaseHandler:
    @staticmethod
    def add_record(db: Session, model: DeclarativeMeta, data: dict) -> bool:
        try:
            new_record = model(**data)
            db.add(new_record)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def edit_record(
        db: Session,
        model: DeclarativeMeta,
        data: dict
    ) -> bool:
        try:
            record = BaseHandler.get_single_record(
                db,
                model,
                "id",
                data["id"]
                )
            if not record:
                raise ValueError("Record doesn't exsists!")
            for key, value in data.items():
                if key != "id" and hasattr(record, key):
                    setattr(record, key, value)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def delete_record(
        db: Session,
        model: DeclarativeMeta,
        search_column: str,
        search_key: Union[int, str]
    ) -> bool:
        try:
            to_delete_record = BaseHandler.get_single_record(
                db, model, search_column, search_key
            )
            db.delete(to_delete_record)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def get_single_record(
        db: Session,
        model: DeclarativeMeta,
        search_column: str,
        search_key: Union[int, str]
    ) -> Optional[DeclarativeMeta]:
        if not hasattr(model, search_column):
            raise ValueError("Wrong search key!")
        record = select(model).where(
            getattr(model, search_column) == search_key
            )
        result = db.execute(record).scalars().first()
        return result
