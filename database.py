from sqlalchemy import create_engine, MetaData


DATABASE_URL = post


engine = create_engine(DATABASE_URL)


metadata = MetaData()