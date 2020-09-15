from . import db

class Item(db.Model): 
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key=True) 
    item_name = db.Column(db.String(300)) 
    count = db.Column(db.Integer)
    