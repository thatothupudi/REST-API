from sqlalchemy import create_engine, Column, String,NUMERIC,VARCHAR,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://user:pass@localhost:5432/pc')
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Computer(Base):
    __tablename__ = 'computers'
    id = Column(Integer, primary_key= True)

    hard_drive = Column(VARCHAR)
    processor = Column(VARCHAR)
    amount_of_ram = Column(VARCHAR)
    maximum_ram = Column(VARCHAR)
    hard_drive_space = Column(VARCHAR)
    form_factor = Column(VARCHAR)

    def __init__(self, hard_drive, processor, amount_of_ram, maximum_ram, hard_drive_capacity, form_factor):
        
        self.hard_drive = hard_drive
        self.processor = processor
        self.amount_of_ram = amount_of_ram
        self.maximum_ram = maximum_ram
        self.hard_drive_capacity = hard_drive_capacity
        self.form_factor = form_factor
        session.commit()
        
    def save_computer(self):
        session.add(self)
        session.commit()

Computer1 = Computer("Berry","Intel Core i5","16GB","16GB","512GB","max")
Computer2 = Computer("Hitachi","Intel Core i7","8GB","16GB","1TB","max")
Computer3 = Computer("HGST","Intel Core i7 6th Gen","32GB","32GB","1B","max")
session.add(Computer1)
session.add(Computer2)
session.add(Computer3)
session.commit()