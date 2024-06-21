from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

# Connection details
user = 'faux'
password = 'PhAcKeJPg3qsfAOC'
host = 'db'
port = '3306'

# Construct the database URL for SQLAlchemy
database_url = f"mariadb+mariadbconnector://{user}:{password}@{host}:{port}"

# Create an SQLAlchemy engine
engine = create_engine(database_url)

# Establish a connection
try:
    with engine.connect() as connection:
        # Execute the 'SHOW DATABASES;' command
        result = connection.execute(text("SHOW DATABASES;"))
        
        # Print the results
        print("Databases:")
        for row in result:
            print(row[0])
except Exception as e:
    print(f"An error occurred: {e}")

# Close the engine
engine.dispose()
