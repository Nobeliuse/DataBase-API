from settings import db

class Battery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))

    def __repr__(self):
        return self.title


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    batteries = db.relationship('Battery', backref='device')

    def __repr__(self):
        return self.title
