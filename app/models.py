from app import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #task and status
    task = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, default=False)

