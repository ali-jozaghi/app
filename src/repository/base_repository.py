from sqlalchemy import select


class BaseRepository:
    def __init__(self, connection):
        self._connection = connection

    def select_one(self, schema, query):
        select_query = select([schema]).where(query)
        result = self._connection.execute(select_query)
        result = result.first()
        if not result:
            return None
        return result
