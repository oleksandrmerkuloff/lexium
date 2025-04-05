from typing import Type

from sqlalchemy.orm import Session, DeclarativeMeta

from .basic import BaseHandler
from ..database.models import Word


class WordHandler(BaseHandler):
    def __init__(self, db: Session, model: Type[DeclarativeMeta] = Word):
        super().__init__(db, model)
