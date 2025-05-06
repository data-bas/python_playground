import pytest
import psycopg2
from testcontainers.postgres import PostgresContainer


@pytest.fixture(
    scope="session")  # setup task welke de container opstart en resources beschikbaar stelt en opruimt na de testen
def postgres_db():
    # Start de PostgreSQL container
    with PostgresContainer("postgres:latest") as postgres:
        conn = psycopg2.connect(
            user=postgres.username,
            password=postgres.password,
            host=postgres.get_container_host_ip(),
            port=postgres.get_exposed_port(5432),
            database=postgres.dbname
        )
        cursor = conn.cursor()
        # Maak de tabel aan
        cursor.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            active BOOLEAN NOT NULL
        );
        """)
        conn.commit()
        yield conn, cursor
        # Sluit de verbinding en cursor af
        cursor.close()
        conn.close()
