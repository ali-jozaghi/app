from sqlalchemy import create_engine, MetaData, Table, Column, Integer, \
    String, ForeignKey, DateTime
from datetime import datetime
from dataclasses import dataclass


metadata = MetaData()

users = Table("users", metadata,
              Column("user_id", Integer, primary_key=True),
              Column("email", String(255), index=True, unique=True),
              Column("fullname", String(255), nullable=False)
              )

tasks = Table("tasks", metadata,
              Column("task_id", Integer, primary_key=True),
              Column("owner_id", ForeignKey("users.user_id")),
              Column("title", String(1000), nullable=False),
              Column("story_points", Integer(), nullable=False),
              Column("details", String(2000)),
              Column("created_at", DateTime(), default=datetime.utcnow)
              )


@dataclass
class DatabaseInfo:
    host: str
    port: int
    username: str
    password: str
    name: str


class Database:
    def __init__(self, database_info: DatabaseInfo):
        self._database_info = database_info

    def connect(self):
        connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            self._database_info.username,
            self._database_info.password,
            self._database_info.host,
            self._database_info.port,
            self._database_info.name
        )
        engine = create_engine(connection_string)

        connection = engine.connect()
        metadata.create_all(engine)
        return connection

