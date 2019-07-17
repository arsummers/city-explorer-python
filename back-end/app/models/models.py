from app import db

class Locations_DB(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)

    def convert_to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name
        }

