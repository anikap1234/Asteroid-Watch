from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, create_engine, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class NearEarthObject(Base):
    __tablename__ = 'near_earth_objects'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    diameter_km = Column(Float, nullable=True)
    is_potentially_hazardous = Column(Boolean, nullable=False)
    close_approaches = relationship('CloseApproachData', back_populates='neo')

class CloseApproachData(Base):
    __tablename__ = 'close_approach_data'
    id = Column(Integer, primary_key=True)
    neo_id = Column(Integer, ForeignKey('near_earth_objects.id'), nullable=False)
    close_approach_date = Column(Date, nullable=False)
    relative_velocity_kph = Column(Float, nullable=False)
    miss_distance_km = Column(Float, nullable=False)
    neo = relationship('NearEarthObject', back_populates='close_approaches')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    alerts = relationship('Alert', back_populates='user')

class Alert(Base):
    __tablename__ = 'alerts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    neo_id = Column(Integer, ForeignKey('near_earth_objects.id'), nullable=False)
    alert_date = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    sent = Column(Boolean, default=False, nullable=False)
    user = relationship('User', back_populates='alerts')

# Database connection setup
DATABASE_URL = "postgresql://username:password@localhost/asteroid_watch"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""def init_db():
    # This will create the tables if they do not already exist
    Base.metadata.create_all(bind=engine)"""

# Example usage
"""if __name__ == "__main__":
    init_db()  # Ensure the database is initialized"""


