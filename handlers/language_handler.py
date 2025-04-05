from typing import Type

from sqlalchemy.orm import Session, DeclarativeMeta

from .basic import BaseHandler
from ..database.models import Language


class LanguageHandler(BaseHandler):
    def __init__(self, db: Session, model: Type[DeclarativeMeta] = Language):
        super().__init__(db, model)
