from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Inject a default __repr__ implementation
def __repr__(self: Base) -> str:  # noqa: N
    all_attrs = (
        f"{attr.key}={getattr(self, attr.key)!r}"
        for attr in self.__table__.columns
        if getattr(self, attr.key) is not None
    )

    return f"{self.__class__.__name__}({', '.join(all_attrs)})"


Base.__repr__ = __repr__
