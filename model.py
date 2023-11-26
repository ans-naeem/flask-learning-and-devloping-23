from . import db

class user(db.model):
    id=db.Column(db.Interger,primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100),unique=True)
