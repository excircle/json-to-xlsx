from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker

# Connection details
user = 'faux'
password = 'PhAcKeJPg3qsfAOC'
host = 'db'
port = '3306'
database = 'faux-db'  # Replace with your actual database name

# Construct the database URL for SQLAlchemy
database_url = f"mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}"

# Create an SQLAlchemy engine
engine = create_engine(database_url)

# Reflect the 'customer' table using the engine connection
metadata = MetaData()
customer_table = Table('customer', metadata, autoload_with=engine)

# Create a session to connect to the database
Session = sessionmaker(bind=engine)
session = Session()

# Query to select all rows from the 'customer' table
try:
    with engine.connect() as connection:
        query = select(customer_table)
        result = connection.execute(query)
        
        # Print the results
        print("Customer Table Rows:")
        for row in result:
            print(row)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    session.close()
    engine.dispose()
