from typing import Type

from sqlalchemy.orm import Session, DeclarativeMeta

from .basic import BaseHandler
from ..database.models import Source


class SourceHandler(BaseHandler):
    def __init__(self, db: Session, model: Type[DeclarativeMeta] = Source):
        super().__init__(db, model)
