from pydantic import BaseSettings


class Setting(BaseSettings):
    database_username: str = ''
    database_password: str = ''
    database_url: str = ''
    database_name: str = 'app_db'
    database_port: int = 0


setting = Setting()
