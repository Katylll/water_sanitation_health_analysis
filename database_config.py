from sqlalchemy import create_engine # type: ignore

# Replace these with your actual database details
DB_USER = "postgres"
DB_PASSWORD = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "Mini project"

def get_engine():
    """
    Create and return a SQLAlchemy engine connected to your PostgreSQL database.
    """
    connection_string = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(connection_string)
