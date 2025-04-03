from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, DateTime, ForeignKey, Text, Boolean

from db_config import Base


class Language(Base):
    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(primary_key=True)
    lang: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    themes: Mapped[list["Theme"]] = relationship(back_populates="language")
    words: Mapped[list["Word"]] = relationship(back_populates="language")
    notes: Mapped[list["Note"]] = relationship(back_populates="language")
    sources: Mapped[list["Source"]] = relationship(back_populates="language")

    def __str__(self) -> str:
        return self.lang

    def __repr__(self) -> str:
        return self.lang


class Theme(Base):
    __tablename__ = "themes"

    id: Mapped[int] = mapped_column(primary_key=True)
    theme: Mapped[str] = mapped_column(String(50), nullable=False)
    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"),
                                             nullable=False)

    language: Mapped["Language"] = relationship(back_populates="themes")
    words: Mapped[list["Word"]] = relationship(back_populates="theme")

    def __str__(self) -> str:
        return self.theme

    def __repr__(self) -> str:
        return self.theme


class Word(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String(50), nullable=False)
    translate: Mapped[str] = mapped_column(String(50), nullable=False)
    know: Mapped[bool] = mapped_column(Boolean, default=False)
    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"),
                                             nullable=False)
    theme_id: Mapped[int] = mapped_column(ForeignKey("themes.id"),
                                          nullable=False)

    theme: Mapped["Theme"] = relationship(back_populates="words")
    language: Mapped["Language"] = relationship(back_populates="words")

    def __str__(self) -> str:
        return f"{self.word} -> {self.translate}"

    def __repr__(self) -> str:
        return self.word


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 default=datetime.today)
    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"),
                                             nullable=False)

    language: Mapped["Language"] = relationship(back_populates="notes")

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title


class Source(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(primary_key=True)
    source_name: Mapped[str] = mapped_column(String(150), nullable=False)
    url: Mapped[str] = mapped_column(String(250))
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 default=datetime.today)
    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"),
                                             nullable=False)

    language: Mapped["Language"] = relationship(back_populates="sources")

    def __str__(self) -> str:
        return self.source_name

    def __repr__(self) -> str:
        return self.source_name
