import sqlalchemy as sa
from extensions import Base
from extensions import engine
from marshmallow_sqlalchemy import ModelSchema


class Coord(Base):
    __tablename__ = "coordinate"
    id = sa.Column(sa.String(20), primary_key=True)
    x = sa.Column(sa.Integer, primary_key=True)
    y = sa.Column(sa.Integer, primary_key=True)


Base.metadata.create_all(engine)


class CoordSchema(ModelSchema):
    class Meta:
        model = Coord


coord_schema = CoordSchema()
coords_schema = CoordSchema(many=True)
