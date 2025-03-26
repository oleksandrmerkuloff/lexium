"""Module what includes a SQLAlchemy models for app"""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Theme(Base):
    """Theme model for SQLAlchemy"""
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True)
    name = Column(String(70), nullable=False)

    words = relationship("Word", back_populates="theme")


class Language(Base):
    """Language model for SQLAlchemy"""
    __tablename__ = "languages"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    words = relationship("Word", back_populates="language")


class Word(Base):
    """Word model for SQLAlchemy"""
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    know = Column(Boolean, default=False)
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=False)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)

    theme = relationship("Theme", back_populates="words")
    language = relationship("Language", back_populates="words")
