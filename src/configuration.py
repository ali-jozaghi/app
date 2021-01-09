from pydantic import BaseSettings


class Setting(BaseSettings):
    database_username: str = 'postgres'
    database_password: str = 'password'
    database_host: str = 'localhost'
    database_name: str = 'postgres'
    database_port: int = 5432


setting = Setting()
