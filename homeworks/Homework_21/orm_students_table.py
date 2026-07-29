from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class OrmStudent(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    course_id = Column(
        Integer,
        ForeignKey("courses.id"),
        nullable=False,
    )

    course = relationship(
        "OrmCourse",
        back_populates="students",
    )

    def __repr__(self):
        return (
            f"OrmStudent(id={self.id}, "
            f"name={self.name!r}, age={self.age}, "
            f"course_id={self.course_id})"
        )
