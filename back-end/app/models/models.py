from sqlalchemy import inspect
from app import db

class ModelToDictMixin:
    def convert_to_dict(self, fields = None):
        inst = inspect(self.__class__)
        fields = fields or [c_attr.key in inst.mapper.column_attrs]

        as_dict = {}

        for field in fields:
            as_dict[field] = getattr(self, field)

        return as_dict


class LocationsModel(ModelToDictMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    formatted_query = db.Column(db.String(256), unique=True)
    latitude = db.Column(db.Float(10.7))
    longitude = db.Column(db.Float(10.7))


    def __repr__(self):
        return f'<Location   {self.formatted_query}>'

    def convert_to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'formatted_query' : self.formatted_query,
            'latitude' : self.latitude,
            'longitude' : self.longitude
        }

