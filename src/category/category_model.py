from src.db import db


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    record = db.relationship('RecordModel', back_populates='category', lazy='dynamic')
