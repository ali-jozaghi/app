import pytest
from src.repository.database import DatabaseInfo, Database


database_info = DatabaseInfo(
    host="localhost",
    port=5422,
    username="postgres",
    password="secret_password",
    name="postgres"
)


@pytest.fixture(scope="session")
def database_connection():
    connection = Database(database_info).connect()
    try:
        yield connection
    finally:
        connection.close()
