from app import db
from datetime import datetime



class Contact(db.Model):
    __tablename__ = 'contact_submissions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    is_read = db.Column(db.Boolean, default=False)
    admin_response = db.Column(db.Text)
    responded_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)