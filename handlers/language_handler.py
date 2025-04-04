from typing import Optional

from sqlalchemy.orm import Session

from ..database.models import Language


class LanguageHandler:
    @staticmethod
    def add_language(db: Session, lang: str) -> bool:
        try:
            new_lang = Language(lang)
            db.add(new_lang)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def edit_language(db: Session, language_id: int, new_lang) -> bool:
        language = LanguageHandler.get_language(language_id)
        try:
            language.lang = new_lang
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def delete_language(db: Session, language_id: int) -> bool:
        try:
            language = LanguageHandler.get_language(language_id)
            db.delete(language)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def get_language(db: Session, language_id: int) -> Optional[Language]:
        language = db.get(Language, language_id)
        return language
