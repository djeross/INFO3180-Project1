from . import db

class MyProperty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(500))
    rooms = db.Column(db.String(15))
    bathrooms = db.Column(db.String(15))
    price= db.Column(db.String(15))
    ptype= db.Column(db.String(15))
    location = db.Column(db.String(100))
    filename = db.Column(db.String(120))

    def __init__(self,title,description,rooms,bathrooms,price,ptype,location,imagename):
        self.title=title
        self.description=description
        self.rooms=rooms
        self.bathrooms=bathrooms
        self.price=price
        self.ptype=ptype
        self.location=location
        self.filename = imagename

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % self.title