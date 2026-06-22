from datetime import date
from . import db

class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    entry_type = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String, nullable=True)
    is_recurring = db.Column(db.Boolean, default=False)
    recurrence_frequency = db.Column(db.String, nullable=True)
    ends_on = db.Column(db.Date, nullable=True)
    attached_individual = db.Column(db.String, nullable=False)