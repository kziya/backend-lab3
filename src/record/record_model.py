from src.db import db


class RecordModel(db.Model):
    __tablename__ = 'record'
    
    id = db.Column(db)
    idUser = db.Column(db.Integer, db.ForeignKey('user.id'))
    idCategory = db.Column(db.Integer, db.ForeignKey('category.id'))
    expenditureAmount = db.Column(db.Float, default=0)
    dateCreated = db.Column(db.DateTime, default=db.func.current_timestamp())
