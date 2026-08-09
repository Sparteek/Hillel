from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class OrmCourse(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(
        String(100),
        nullable=False,
        unique=True,
    )

    students = relationship(
        "OrmStudent",
        back_populates="course",
    )

    def __repr__(self):
        return f"OrmCourse(id={self.id}, name={self.name!r})"
