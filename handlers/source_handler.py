from typing import Optional

from sqlalchemy.orm import Session

from ..database.models import Source


class SourceHandler:
    @staticmethod
    def add_source(db: Session, source_data: dict) -> bool:
        try:
            new_source = Source(**source_data)
            db.add(new_source)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def edit_source(db: Session, source_id: int, **kwargs) -> bool:
        source = SourceHandler.get_source(source_id)
        source_attrs = dir(source)
        try:
            for key, value in kwargs.items():
                if key in source_attrs and key != "id":
                    setattr(source, key, value)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def delete_source(db: Session, source_id: int) -> bool:
        try:
            source = SourceHandler.get_source(source_id)
            db.delete(source)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def get_source(db: Session, source_id: int) -> Optional[Source]:
        source = db.get(Source, source_id)
        return source
