from app import db

class LocationsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    formatted_query = db.Column(db.String(256), unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def convert_to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'formatted_query' : self.formatted_query,
            'latitude' : self.latitude,
            'longitude' : self.longitude
        }

