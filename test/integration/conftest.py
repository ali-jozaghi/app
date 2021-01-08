from .test_startup import database_info
from src.common.docker import DockerContainer
from time import sleep


def wait_for_the_running_status(container, timeout=150, stop_time=4, elapsed_time=0):
    while elapsed_time < timeout:
        sleep(stop_time)
        elapsed_time += stop_time
        if container.is_ready():
            break


def pytest_sessionstart(session):
    print("Setting up the database container...")
    environment_variables = {
        "POSTGRES_PASSWORD": database_info.password,
        "POSTGRES_DB": database_info.name
    }
    container = DockerContainer("postgres", '5432/tcp', database_info.port, environment_variables)
    container.create()
    wait_for_the_running_status(container)
    print("Database is ready!!!")
    session.container = container


def pytest_sessionfinish(session, exitstatus):
    print("\nTearing down the database.")
    session.container.tear_down()
    print("Done.")


