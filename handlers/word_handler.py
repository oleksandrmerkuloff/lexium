from typing import Optional

from sqlalchemy.orm import Session

from ..database.models import Word


class WordHandler:
    @staticmethod
    def add_word(db: Session, word_data: dict) -> bool:
        try:
            new_word = Word(**word_data)
            db.add(new_word)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def edit_word(db: Session, word_id: int, **kwargs) -> bool:
        word = WordHandler.get_single_word(word_id)
        word_attrs = dir(word)
        try:
            for key, value in kwargs.items():
                if key in word_attrs and key != "id":
                    setattr(word, key, value)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def delete_word(db: Session, word_id: int) -> bool:
        try:
            word = WordHandler.get_single_word(word_id)
            db.delete(word)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def get_single_word(db: Session, word_id: int) -> Optional[Word]:
        word = db.get(Word, word_id)
        return word
