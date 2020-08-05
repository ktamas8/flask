from wtfforms import db

class Flavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    vcpu = db.Column(db.Integer, unique=False, nullable=False)
    disk = db.Column(db.Integer, unique=False, nullable=False)
    ram = db.Column(db.Integer, unique=False, nullable=False)
    instances = db.relationship('Instance', backref='resource', lazy=True)

    def __repr__(self):
        return f"Flavor('{self.id}', '{self.name}')"

class Instance(db.Model):
    uuid = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    state = db.Column(db.String(20), unique=False, nullable=False)
    flavor_id = db.Column(db.Integer, db.ForeignKey('flavor.id'), nullable=False)

    def __repr__(self):
        return f"Instance('{self.uuid}', '{self.name}', '{self.state}')"
