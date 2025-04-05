from typing import Type

from sqlalchemy.orm import Session, DeclarativeMeta

from .basic import BaseHandler
from ..database.models import Note


class NoteHandler(BaseHandler):
    def __init__(self, db: Session, model: Type[DeclarativeMeta] = Note):
        super().__init__(db, model)
