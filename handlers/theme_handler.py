from typing import Optional

from sqlalchemy.orm import Session

from ..database.models import Theme


class ThemeHandler:
    @staticmethod
    def add_theme(db: Session, theme: str, language_id: int) -> bool:
        try:
            new_theme = Theme(name=theme, language_id=language_id)
            db.add(new_theme)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def edit_theme(db: Session, theme_id: int, name: str) -> bool:
        try:
            theme = ThemeHandler.get_theme(theme_id)
            theme.name = name
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def delete_theme(db: Session, theme_id: int) -> bool:
        try:
            theme = ThemeHandler.get_theme(theme_id)
            db.delete(theme)
        except Exception:
            db.rollback()
            return False
        else:
            db.commit()
            return True

    @staticmethod
    def get_theme(db: Session, theme_id: int) -> Optional[Theme]:
        theme = db.get(Theme, theme_id)
        return theme
