from db import db
from datetime import datetime, UTC


class RevokedTokenModel(db.Model):
    __tablename__ = "revoked_tokens"

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120), unique=True, nullable=False)
    revoked_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC))
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # user = db.relationship("UserModel", back_populates="revoked_tokens")
