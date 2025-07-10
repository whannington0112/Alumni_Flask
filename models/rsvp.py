from app import db
from datetime import datetime



class RSVP(db.Model):
    __tablename__ = 'rsvps'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    status = db.Column(db.String(20))  # 'attending', 'not_attending', 'maybe'
    rsvp_date = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)
    __table_args__ = (db.UniqueConstraint('user_id', 'event_id'),) 