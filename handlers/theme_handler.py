from typing import Type

from sqlalchemy.orm import Session, DeclarativeMeta

from .basic import BaseHandler
from ..database.models import Theme


class ThemeHandler(BaseHandler):
    def __init__(self, db: Session, model: Type[DeclarativeMeta] = Theme):
        super().__init__(db, model)
