from typing import Optional

from sqlalchemy.orm import Session

from ..database.models import Source


class NoteHandler:
    @staticmethod
    def add_note(db: Session, note_data: dict) -> bool:
        try:
            new_note = Source(**note_data)
            db.add(new_note)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def edit_note(db: Session, note_id: int, **kwargs) -> bool:
        note = NoteHandler.get_note(note_id)
        note_attrs = dir(note)
        try:
            for key, value in kwargs.items():
                if key in note_attrs and key != "id":
                    setattr(note, key, value)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def delete_note(db: Session, note_id: int) -> bool:
        try:
            note = NoteHandler.get_note(note_id)
            db.delete(note)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def get_note(db: Session, note_id: int) -> Optional[Source]:
        note = db.get(Source, note_id)
        return note
