import aiosqlite
from database.queries import Queries

class Database:
    def __init__(self, path):
        self.path = path

    async def create_tables(self):
        async with aiosqlite.connect(self.path) as conn:
            async with conn.cursor() as cur:
                await cur.execute(Queries.CREATE_SURVEY_TABLE)
                await cur.execute(Queries.DROP_CATEGORIES_TABLE)
                await cur.execute(Queries.DROP_DISHES_TABLE)
                await cur.execute(Queries.CREATE_CATEGORIES_TABLE)
                await cur.execute(Queries.CREATE_DISHES_TABLE)
                await cur.execute(Queries.POPULATE_CATEGORY)
                await cur.execute(Queries.POPULATE_DISHES)

                await conn.commit()

    async def execute(self, query, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query, params)
            await conn.commit()

    async def main():
        db = Database('db1.sqlite')
        await db.create_tables()

        # Пример запроса INSERT для таблицы "review"
        query = "INSERT INTO db.sqlite (name, phone, visit_data, food_quality, cleanliness, comments) VALUES (?, ?, ?, ?, ?, ?)"
        params = ('Айдай', '0709331013', '12-09-2022', '5', '4', 'очень уютно')
        await db.execute(query, params)

    if __name__ == "__main__":
        import asyncio
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
